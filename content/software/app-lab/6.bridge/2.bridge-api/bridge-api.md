---
title: Bridge API Reference
description: Comprehensive reference for the Arduino App Lab Bridge RPC API, covering C++, Python, and data type mappings.
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

Use the `Bridge` library to enable bidirectional communication between the high-level Python logic and the real-time Arduino sketch. This Remote Procedure Call (RPC) layer allows you to exchange data, trigger functions, and synchronize tasks across processors.

The Arduino Router (`arduino-router`) background Linux service routes every call between the processors, using a star topology and [MessagePack-RPC](https://github.com/msgpack-rpc/msgpack-rpc/blob/master/spec.md). Both the sketch and the Python script are clients of the router: each one can provide functions and call the functions provided by the other.

## Hardware and System Specifications

On the UNO Q, the Bridge uses the following hardware resources to maintain the communication link:

- **Linux Interface:** `/dev/ttyHS1`.
- **MCU Interface:** `Serial1`.
- **Baud Rate:** 115200 bps.
- **Maximum Message Size:** 256 bytes per call from the sketch.

Do not attempt to open `/dev/ttyHS1` (on Linux) or `Serial1` (on Arduino/Zephyr) in application code. The `arduino-router` service exclusively locks these interfaces. Attempting direct access causes the Bridge to fail.

## C++ API (MCU / Sketch)

The C++ implementation is provided by the `Arduino_RouterBridge` library, which is included by default on boards with Zephyr core 0.55.0 or later. The global `Bridge` object manages the RPC clients and servers on the microcontroller.

```cpp
#include "Arduino_RouterBridge.h"
```

### `begin()`

Initializes the Bridge and its serial transport. Call this method in `setup()` before using any other Bridge method.

#### Parameters

None.

#### Returns

`bool`: `true` if the connection with the router was established.

### `call(String, Args...)`

Invokes a function provided by the Linux side.

The call is sent and its response awaited when you read the result with `result()`, or when the returned object goes out of scope. A plain `Bridge.call("method", value);` statement therefore blocks until the Linux side responds.

#### Parameters

- `method` `String`: The name of the provided function to invoke.
- `args` `Args...`: A variable number of arguments to pass to the function.

#### Returns

`RpcCall`: An object representing the call. It converts to `bool` (`true` if the call succeeded), so you can write `if (Bridge.call("method")) { ... }`.

#### Example

```cpp
int temperature;
if (Bridge.call("get_temperature").result(temperature)) {
  Monitor.println(temperature);
}
```

### `RpcCall.result(Variable)`

Sends the call if it hasn't been sent yet, waits for the response, and stores the returned value in the provided variable. Each call can be read only once.

#### Parameters

- `variable` `Variable`: The variable to store the returned value. Omit it for functions that return nothing.

#### Returns

`bool`: `true` if the call succeeded. If it failed, use `isError()`, `getErrorCode()`, and `getErrorMessage()` on the `RpcCall` object to inspect the error.

### `notify(String, Args...)`

Invokes a function on the Linux side without waiting for a response. This provides "fire-and-forget" semantics for asynchronous data transmission. Messages exceeding the 256-byte limit are dropped.

#### Parameters

- `method` `String`: The name of the function to notify.
- `args` `Args...`: A variable number of arguments to pass.

#### Returns

None.

### `provide(String, Function)`

Exposes a local MCU function to the Linux environment. The provided function executes in the high-priority background RPC thread. Functions registered with this method must remain short and thread-safe.

<Alert type="danger">

**Danger:** Do not use `Bridge.call()` or `Monitor.print()` inside functions registered with `Bridge.provide()`. Initiating a new communication while responding to one causes system deadlocks. Use `provide_safe()` instead.

</Alert>

#### Parameters

- `name` `String`: The name to register the function under.
- `function` `Function`: The callback function to execute.

#### Returns

`bool`: `true` if the function was registered with the router.

### `provide_safe(String, Function)`

Exposes a local MCU function to the Linux environment and ensures it executes within the main `loop()` context. Use this method if the callback function interacts with standard Arduino APIs, such as `digitalWrite`, `Monitor`, or `Serial`, to prevent concurrency crashes.

#### Parameters

- `name` `String`: The name to register the function under.
- `function` `Function`: The callback function to execute safely.

#### Returns

`bool`: `true` if the function was registered with the router.

## Python API (MPU / Linux)

The Python implementation requires importing the `Bridge` class from the `arduino.app_utils` module:

```python
from arduino.app_utils import Bridge
```

The Bridge connects to the Arduino Router the first time you use it. If the router cannot be reached within 5 seconds, an `AppError` is raised, with a hint to check that the `arduino-router` service is running.

### `Bridge.call(str, *args, timeout=10)`

Invokes a function provided by the microcontroller and blocks until the microcontroller returns a result.

#### Parameters

- `method_name` `str`: The name of the function to call.
- `*args` `Any`: A variable number of arguments to pass to the function.
- `timeout` `float | None`: The maximum time to wait for a response, in seconds. Defaults to `10`. Use `None` to wait indefinitely.

#### Returns

`Any`: The result returned by the microcontroller function.

#### Exceptions

- `ValueError`: The microcontroller answered with an error, for example because the function is not provided. The exception is an `arduino.router_bridge.RpcError` with the error `code` and `message`.
- `TimeoutError`: No response arrived within `timeout`.
- `ConnectionError`: The connection dropped while waiting for the response.
- `RuntimeError`: The call was made from inside a provided handler (nested calls are not supported), or failed unexpectedly.

#### Example

```python
temperature = Bridge.call("get_temperature", timeout=2)
```

### `Bridge.notify(str, *args)`

Sends data to a function provided by the microcontroller without waiting for a return value. Notifications are best-effort: if the router is not connected, the notification is dropped.

#### Parameters

- `method_name` `str`: The name of the function to notify.
- `*args` `Any`: A variable number of arguments to pass.

#### Returns

None.

### `Bridge.provide(str, Callable)`

Registers a Python function that the microcontroller can call. The function is registered as soon as the router is connected, and registered again automatically after a reconnection.

Provided functions run one at a time on a dedicated thread. They can send notifications with `Bridge.notify()`, but must not use `Bridge.call()`, `Bridge.provide()`, or `Bridge.unprovide()`, which raise a `RuntimeError`.

#### Parameters

- `method_name` `str`: The name to register the function under.
- `handler` `Callable`: The Python function to invoke.

#### Returns

None.

#### Exceptions

- `ValueError`: `handler` is not callable, or another client (for example, the sketch) already provides a function with the same name.

### `Bridge.unprovide(str)`

Removes a function previously registered with `Bridge.provide()`, so the microcontroller can no longer call it.

#### Parameters

- `method_name` `str`: The name the function was registered under.

#### Returns

None.

### Decorators

The `arduino.app_utils` module also provides decorators that turn plain Python functions into Bridge calls. By default, the RPC name is the name of the decorated function. Only positional arguments are supported.

```python
from arduino.app_utils import App, call, notify, provide

@call(timeout=3)
def get_temperature() -> float: ...  # Body not needed: calls "get_temperature" on the MCU

@notify("set_led_state")
def set_led(state: bool): ...  # Body not needed: notifies "set_led_state" on the MCU

@provide()
def get_country(lon: str, lat: str) -> str:
    # The MCU can call "get_country"
    return "Italy"

def loop():
    set_led(get_temperature() > 25)

App.run(user_loop=loop)
```

- `@call(method_name=None, timeout=10)`: Calling the function sends an RPC call and returns the result. Pass `timeout=` when calling the function to override the default.
- `@notify(method_name=None)`: Calling the function sends a notification.
- `@provide(method_name=None)`: Registers the function so that the microcontroller can call it.

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

The `Monitor` object sends text from the sketch to the **Serial Monitor** tab of the App Lab console, and receives the text you type there. It works like a standard Arduino `Stream`, and the data travels over the Bridge.

<Alert type="info">

**Note:** On boards with Zephyr core 0.55.0 or later, `Serial` is routed to the Serial Monitor too, so `Serial.print()` and `Monitor.print()` produce the same output.

</Alert>

### `begin()`

Initializes the Monitor interface. Any baud rate argument is ignored.

#### Parameters

None.

#### Returns

`bool`: `true` if the Monitor is connected.

### `print(Any)`

Transmits data to the Serial Monitor.

#### Parameters

- `value` `Any`: The data to transmit.

#### Returns

`size_t`: The number of bytes written.

### `println(Any)`

Transmits data to the Serial Monitor and appends a newline character to the output.

#### Parameters

- `value` `Any`: The data to transmit.

#### Returns

`size_t`: The number of bytes written.

### `available()`

Returns the number of bytes received from the Serial Monitor and ready to read.

#### Parameters

None.

#### Returns

`int`: The number of bytes available.

### `read()`

Reads the next byte received from the Serial Monitor.

#### Parameters

None.

#### Returns

`int`: The next byte of data, or `-1` if no data is available.
