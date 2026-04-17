---
title: Bridge API Reference
description: Comprehensive reference for the Arduino UNO Q Bridge RPC API, covering C++, Python, and data type mappings.
overwriteSidebar: Bridge API
tags:
  - Reference
  - Bridge
  - RPC
  - API
  - Python
  - C++
  - MsgPack
---

The `Bridge` library provides a Remote Procedure Call (RPC) communication layer for the Arduino UNO Q. It enables bidirectional data exchange between the Qualcomm QRB2210 microprocessor (MPU) running Linux and the STM32U585 microcontroller (MCU) running Zephyr RTOS.

The Arduino Router (`arduino-router`) background Linux service manages the underlying network using a Star Topology and MessagePack RPC.

## Hardware and System Specifications

The Bridge infrastructure claims specific hardware resources to maintain the communication link.

* **Linux Interface:** `/dev/ttyHS1`.
* **MCU Interface:** `Serial1`.
* **Baud Rate:** 115200 bps.
* **Maximum Message Size:** 256 bytes.

Do not attempt to open `/dev/ttyHS1` (on Linux) or `Serial1` (on Arduino/Zephyr) in application code. The `arduino-router` service exclusively locks these interfaces. Attempting direct access causes the Bridge to fail.

## C++ API (MCU / Sketch)

The C++ implementation requires the `Arduino_RouterBridge.h` header file. The `BridgeClass` manages the RPC clients and servers on the microcontroller.

### `begin()`

Initializes the bridge and the internal serial transport. Applications call this method in the `setup()` function before utilizing other Bridge methods.

#### Parameters

None.

#### Returns

None.

### `call(String, Args...)`

Invokes a registered function on the Linux side and waits for a result.

#### Parameters

* `method` `String`: The name of the registered method to invoke.
* `args` `Args...`: A variable number of arguments to pass to the method.

#### Returns

`RpcCall`: An object representing the asynchronous RPC.

### `RpcCall.result(Variable)`

Waits for the response, extracts the return value into the provided variable, and propagates error codes if the call fails.

#### Parameters

* `variable` `Variable`: The variable to store the extracted return value.

#### Returns

None.

### `notify(String, Args...)`

Invokes a function on the Linux side without waiting for a response. This provides "fire-and-forget" semantics for asynchronous data transmission. It drops oversized messages exceeding the 256-byte limit.

#### Parameters

* `method` `String`: The name of the method to notify.
* `args` `Args...`: A variable number of arguments to pass.

#### Returns

None.

### `provide(String, Function)`

Exposes a local MCU function to the Linux environment. The provided function executes in the high-priority background RPC thread. Functions registered with this method must remain short and thread-safe.

<Alert type="danger">**Danger:** Do not use `Bridge.call()` or `Monitor.print()` inside functions registered with `Bridge.provide()`. Initiating a new communication while responding to one causes system deadlocks.</Alert>

#### Parameters

* `name` `String`: The name to register the function under.
* `function` `Function`: The callback function to execute.

#### Returns

None.

### `provide_safe(String, Function)`

Exposes a local MCU function to the Linux environment and ensures it executes within the main `loop()` context. Applications use this method if the callback function interacts with standard Arduino APIs, such as `digitalWrite` or `Serial`, to prevent concurrency crashes.

#### Parameters

* `name` `String`: The name to register the function under.
* `function` `Function`: The callback function to execute safely.

#### Returns

None.

## Python API (MPU / Linux)

The Python implementation requires importing the `Bridge` class from the `arduino.app_utils` module.

### `call(str, *args)`

Invokes a registered function on the microcontroller and blocks execution until the MCU returns a result.

#### Parameters

* `method_name` `str`: The name of the method to call.
* `*args` `Any`: A variable number of arguments to pass to the method.

#### Returns

`Any`: The result returned by the MCU function.

#### Exceptions

* `ValueError`: Raised for requests exceeding the 256-byte limit.

### `notify(str, *args)`

Sends data to a registered function on the microcontroller without blocking execution or waiting for a return value.

#### Parameters

* `method_name` `str`: The name of the method to notify.
* `*args` `Any`: A variable number of arguments to pass.

#### Returns

None.

### `provide(str, Callable)`

Registers a Python function to receive calls from the microcontroller. When the MCU sends a request matching the `"method_name"` tag, the Python environment invokes the corresponding function.

#### Parameters

* `method_name` `str`: The tag/name to register the function under.
* `function` `Callable`: The Python function to invoke.

#### Returns

None.

## MsgPack Data Type Mappings

The Bridge library uses MsgPack to automatically serialize and deserialize data types between Python and C++.

| Python Type | C++ Type |
| :--- | :--- |
| `bool` | `bool` |
| `int` | `int8_t`, `int16_t`, `int32_t`, `uint8_t`, `uint16_t`, `uint32_t` |
| `float` | `float`, `double` |
| `str` | `char*`, `String` |
| `list` | `std::vector`, `std::array`, `std::list` |
| `dict` | `std::map` |
| `bytes` | `std::vector<uint8_t>`, `arduino::msgpack::arr_t<uint8_t>` |
| `None` | `void` |

## Monitor API

The `Monitor` object replaces the traditional `Serial` object for USB CDC serial port communication in Arduino App Lab. The Linux side utilizes the `mon/write` RPC method to send text streams to the MCU acting as a virtual Serial Monitor.

### `begin()`

Initializes the Monitor interface.

#### Parameters

None.

#### Returns

None.

### `print(Any)`

Transmits data to the Serial Monitor.

#### Parameters

* `value` `Any`: The data to transmit.

#### Returns

None.

### `println(Any)`

Transmits data to the Serial Monitor and appends a newline character to the output.

#### Parameters

* `value` `Any`: The data to transmit.

#### Returns

None.

### `read()`

Reads incoming serial data from the queue.

#### Parameters

None.

#### Returns

`int`: Returns the next byte of data.

<Alert type="info">**Note:** The current C++ implementation of `Monitor.read()` returns `0` instead of `-1` when the queue is empty, which differs from the standard `Stream` class specification.</Alert>
