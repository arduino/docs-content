# MicroPython LIS3DH Accelerometer Library
# Authors: Matt Trentini, Seon Rozenblum
# Based on the Adafruit LIS3DH Accelerometer CircuitPython Driver
# Based on the Arduino LIS3DH driver from:
#   https://github.com/adafruit/Adafruit_LIS3DH/
# Author: Tony DiCola
# License: MIT License (https://en.wikipedia.org/wiki/MIT_License)
"""
`lis3dh`
====================================================

MicroPython library for the LIS3DH accelerometer.

* Author(s): Tony DiCola, Matt Trentini, Seon Rozenblum
"""

import time
import math
try:
    from collections import namedtuple
except ImportError:
    from ucollections import namedtuple
try:
    import struct
except ImportError:
    import ustruct as struct

from micropython import const

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/TinyPICO/micropython-LIS3DH.git"

# Register addresses:
_REG_OUTADC1_L   = const(0x08)
_REG_WHOAMI      = const(0x0F)
_REG_TEMPCFG     = const(0x1F)
_REG_CTRL1       = const(0x20)
_REG_CTRL3       = const(0x22)
_REG_CTRL4       = const(0x23)
_REG_CTRL5       = const(0x24)
_REG_OUT_X_L     = const(0x28)
_REG_INT1SRC     = const(0x31)
_REG_CLICKCFG    = const(0x38)
_REG_CLICKSRC    = const(0x39)
_REG_CLICKTHS    = const(0x3A)
_REG_TIMELIMIT   = const(0x3B)
_REG_TIMELATENCY = const(0x3C)
_REG_TIMEWINDOW  = const(0x3D)

# Register value constants:
RANGE_16_G               = const(0b11)    # +/- 16g
RANGE_8_G                = const(0b10)    # +/- 8g
RANGE_4_G                = const(0b01)    # +/- 4g
RANGE_2_G                = const(0b00)    # +/- 2g (default value)
DATARATE_1344_HZ         = const(0b1001)  # 1.344 KHz
DATARATE_400_HZ          = const(0b0111)  # 400Hz
DATARATE_200_HZ          = const(0b0110)  # 200Hz
DATARATE_100_HZ          = const(0b0101)  # 100Hz
DATARATE_50_HZ           = const(0b0100)  # 50Hz
DATARATE_25_HZ           = const(0b0011)  # 25Hz
DATARATE_10_HZ           = const(0b0010)  # 10 Hz
DATARATE_1_HZ            = const(0b0001)  # 1 Hz
DATARATE_POWERDOWN       = const(0)
DATARATE_LOWPOWER_1K6HZ  = const(0b1000)
DATARATE_LOWPOWER_5KHZ   = const(0b1001)

# Other constants
STANDARD_GRAVITY = 9.806
DEV_ID = 0x33

# the named tuple returned by the class
AccelerationTuple = namedtuple("acceleration", ("x", "y", "z"))

class LIS3DH:
    """Driver base for the LIS3DH accelerometer."""
    def __init__(self, int1=None, int2=None):
        # Check device ID.
        device_id = self._read_register_byte(_REG_WHOAMI)
        if device_id != 0x33:
            raise RuntimeError('Failed to find LIS3DH!')
        # Reboot
        self._write_register_byte(_REG_CTRL5, 0x80)
        time.sleep(0.01)  # takes 5ms
        # Enable all axes, normal mode.
        self._write_register_byte(_REG_CTRL1, 0x07)
        # Set 400Hz data rate.
        self.data_rate = DATARATE_400_HZ
        # High res & BDU enabled.
        self._write_register_byte(_REG_CTRL4, 0x88)
        # Enable ADCs.
        self._write_register_byte(_REG_TEMPCFG, 0x80)
        # Latch interrupt for INT1
        self._write_register_byte(_REG_CTRL5, 0x08)

        # Initialise interrupt pins
        self._int1 = int1
        self._int2 = int2

    @property
    def data_rate(self):
        """The data rate of the accelerometer.  Can be DATARATE_400_HZ, DATARATE_200_HZ,
           DATARATE_100_HZ, DATARATE_50_HZ, DATARATE_25_HZ, DATARATE_10_HZ,
           DATARATE_1_HZ, DATARATE_POWERDOWN, DATARATE_LOWPOWER_1K6HZ, or
           DATARATE_LOWPOWER_5KHZ."""
        ctl1 = self._read_register_byte(_REG_CTRL1)
        return (ctl1 >> 4) & 0x0F

    @data_rate.setter
    def data_rate(self, rate):
        ctl1 = self._read_register_byte(_REG_CTRL1)
        ctl1 &= ~(0xF0)
        ctl1 |= rate << 4
        self._write_register_byte(_REG_CTRL1, ctl1)

    @property
    def range(self):
        """The range of the accelerometer.  Can be RANGE_2_G, RANGE_4_G, RANGE_8_G, or
           RANGE_16_G."""
        ctl4 = self._read_register_byte(_REG_CTRL4)
        return (ctl4 >> 4) & 0x03

    @range.setter
    def range(self, range_value):
        ctl4 = self._read_register_byte(_REG_CTRL4)
        ctl4 &= ~0x30
        ctl4 |= range_value << 4
        self._write_register_byte(_REG_CTRL4, ctl4)

    @property
    def acceleration(self):
        """The x, y, z acceleration values returned in a 3-tuple and are in m / s ^ 2."""
        divider = 1
        accel_range = self.range
        if accel_range == RANGE_16_G:
            divider = 1365
        elif accel_range == RANGE_8_G:
            divider = 4096
        elif accel_range == RANGE_4_G:
            divider = 8190
        elif accel_range == RANGE_2_G:
            divider = 16380

        x, y, z = struct.unpack('<hhh', self._read_register(_REG_OUT_X_L | 0x80, 6))

        # convert from Gs to m / s ^ 2 and adjust for the range
        x = (x / divider) * STANDARD_GRAVITY
        y = (y / divider) * STANDARD_GRAVITY
        z = (z / divider) * STANDARD_GRAVITY

        return AccelerationTuple(x, y, z)

    def shake(self, shake_threshold=30, avg_count=10, total_delay=0.1):
        """
        Detect when the accelerometer is shaken. Optional parameters:

        :param shake_threshold: Increase or decrease to change shake sensitivity. This
                                requires a minimum value of 10. 10 is the total
                                acceleration if the board is not moving, therefore
                                anything less than 10 will erroneously report a constant
                                shake detected. (Default 30)

        :param avg_count: The number of readings taken and used for the average
                          acceleration. (Default 10)

        :param total_delay: The total time in seconds it takes to obtain avg_count
                            readings from acceleration. (Default 0.1)
         """
        shake_accel = (0, 0, 0)
        for _ in range(avg_count):
            # shake_accel creates a list of tuples from acceleration data.
            # zip takes multiple tuples and zips them together, as in:
            # In : zip([-0.2, 0.0, 9.5], [37.9, 13.5, -72.8])
            # Out: [(-0.2, 37.9), (0.0, 13.5), (9.5, -72.8)]
            # map applies sum to each member of this tuple, resulting in a
            # 3-member list. tuple converts this list into a tuple which is
            # used as shake_accel.
            shake_accel = tuple(map(sum, zip(shake_accel, self.acceleration)))
            time.sleep(total_delay / avg_count)
        avg = tuple(value / avg_count for value in shake_accel)
        total_accel = math.sqrt(sum(map(lambda x: x * x, avg)))
        return total_accel > shake_threshold

    def read_adc_raw(self, adc):
        """Retrieve the raw analog to digital converter value.  ADC must be a
        value 1, 2, or 3.
        """
        if adc < 1 or adc > 3:
            raise ValueError('ADC must be a value 1 to 3!')

        return struct.unpack('<h', self._read_register((_REG_OUTADC1_L+((adc-1)*2)) | 0x80, 2))[0]

    def read_adc_mV(self, adc): 
        """Read the specified analog to digital converter value in millivolts.
        ADC must be a value 1, 2, or 3.  NOTE the ADC can only measure voltages
        in the range of ~900-1200mV!
        """
        raw = self.read_adc_raw(adc)
        # Interpolate between 900mV and 1800mV, see:
        # https://learn.adafruit.com/adafruit-lis3dh-triple-axis-accelerometer-breakout/wiring-and-test#reading-the-3-adc-pins
        # This is a simplified linear interpolation of:
        # return y0 + (x-x0)*((y1-y0)/(x1-x0))
        # Where:
        #   x = ADC value
        #   x0 = -32512
        #   x1 = 32512
        #   y0 = 1800
        #   y1 = 900
        return 1800+(raw+32512)*(-900/65024)

    @property
    def tapped(self):
        """
        True if a tap was detected recently. Whether its a single tap or double tap is
        determined by the tap param on ``set_tap``. ``tapped`` may be True over
        multiple reads even if only a single tap or single double tap occurred if the
        interrupt (int) pin is not specified.

        The following example uses ``i2c`` and specifies the interrupt pin:

        .. code-block:: python

            import adafruit_lis3dh
            import digitalio

            i2c = busio.I2C(board.SCL, board.SDA)
            int1 = digitalio.DigitalInOut(board.D11) # pin connected to interrupt
            lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
            lis3dh.range = adafruit_lis3dh.RANGE_8_G

        """
        if self._int1 and not self._int1.value:
            return False
        raw = self._read_register_byte(_REG_CLICKSRC)
        return raw & 0x40 > 0

    def set_tap(self, tap, threshold, *,
                time_limit=10, time_latency=20, time_window=255, click_cfg=None):
        """
        The tap detection parameters.

        .. note:: Tap related registers are called ``CLICK_`` in the datasheet.

        :param int tap: 0 to disable tap detection, 1 to detect only single
                        taps, and 2 to detect only double taps.

        :param int threshold: A threshold for the tap detection.  The higher the value
                              the less sensitive the detection.  This changes based on
                              the accelerometer range.  Good values are 5-10 for 16G,
                              10-20 for 8G, 20-40 for 4G, and 40-80 for 2G.

        :param int time_limit: TIME_LIMIT register value (default 10).
        :param int time_latency: TIME_LATENCY register value (default 20).
        :param int time_window: TIME_WINDOW register value (default 255).
        :param int click_cfg: CLICK_CFG register value.
        """
        if (tap < 0 or tap > 2) and click_cfg is None:
            raise ValueError('Tap must be 0 (disabled), 1 (single tap), or 2 (double tap)!')
        if threshold > 127 or threshold < 0:
            raise ValueError('Threshold out of range (0-127)')

        ctrl3 = self._read_register_byte(_REG_CTRL3)
        if tap == 0 and click_cfg is None:
            # Disable click interrupt.
            self._write_register_byte(_REG_CTRL3, ctrl3 & ~(0x80))  # Turn off I1_CLICK.
            self._write_register_byte(_REG_CLICKCFG, 0)
            return
        else:
            self._write_register_byte(_REG_CTRL3, ctrl3 | 0x80)  # Turn on int1 click output

        if click_cfg is None:
            if tap == 1:
                click_cfg = 0x15  # Turn on all axes & singletap.
            if tap == 2:
                click_cfg = 0x2A  # Turn on all axes & doubletap.
        # Or, if a custom click configuration register value specified, use it.
        self._write_register_byte(_REG_CLICKCFG, click_cfg)
        self._write_register_byte(_REG_CLICKTHS, 0x80 | threshold)
        self._write_register_byte(_REG_TIMELIMIT, time_limit)
        self._write_register_byte(_REG_TIMELATENCY, time_latency)
        self._write_register_byte(_REG_TIMEWINDOW, time_window)

    def _read_register_byte(self, register):
        # Read a byte register value and return it.
        return self._read_register(register, 1)[0]

    def _read_register(self, register, length):
        # Read an arbitrarily long register (specified by length number of
        # bytes) and return a bytearray of the retrieved data.
        # Subclasses MUST implement this!
        raise NotImplementedError

    def _write_register_byte(self, register, value):
        # Write a single byte register at the specified register address.
        # Subclasses MUST implement this!
        raise NotImplementedError

class LIS3DH_I2C(LIS3DH):
    """Driver for the LIS3DH accelerometer connected over I2C."""

    def __init__(self, i2c, *, address=0x18, int1=None, int2=None):
        self._i2c = i2c
        self._address = address
        super().__init__(int1=int1, int2=int2)

    def _read_register(self, register, length):
        return self._i2c.readfrom_mem(self._address, register, length)

    def _write_register_byte(self, register, value):
        self._i2c.writeto_mem(self._address, register, bytes([value]))

    def device_check(self):
        who = self._i2c.readfrom_mem(self._address, _REG_WHOAMI, True)[0]
        if who == DEV_ID:
            # We found the LIS3DH
            return True
        else:
            print("unknown dev: 0x{:02X}".format(who))
            return False