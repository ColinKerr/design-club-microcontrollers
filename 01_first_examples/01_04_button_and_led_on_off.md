# Button and LED On and Off Switch


Toggle an LED on and off with a push button — press once to turn ON, press again to turn OFF. Unlike [Button & LED](./01_03_button_and_led.md), the LED state persists after releasing the button. 

Uses the same components and circuit as [Button & LED](./01_03_button_and_led.md).

## New Concepts

- functions
- classes


### Concept: Functions

A function encapsulates code so it can be used multiple times using just the function name.  It also makes code easier to read and understand.

Defining a function

```python
def reverseGPIO():
    if led.value():
        led.value(0)
    else:
        led.value(1)
```

Calling a function

```python
reverseGPIO()
```

### Concept: Classes

A class encapsulates data and code so it can be reused and like a function makes programs easier to read and understand.

This project uses a `Button` class (in `button.py`). Creating an object from the class sets up the pin and remembers which function to call:

```python
button = Button(13, reverseGPIO)   # pin 13, call reverseGPIO when pressed
```



## Component List & Circuit Diagram

*Circuit and components are identical to [Button & LED](./01_03_button_and_led.md)*

## Code

**File:** [`01_first_examples/code/ButtonAndLed_OnOff.py`](./code/ButtonAndLed_OnOff.py)

```python
from button import Button
from machine import Pin

def reverseGPIO():
    if led.value():
        led.value(0)
    else:
        led.value(1)

led = Pin(2, Pin.OUT)

button = Button(13, reverseGPIO)
```

## How to Run

### Online
1. Open Thonny → `01_first_examples/code/`.
2. Right-click `button.py` → **Upload to /** if it isn't already on the device.
3. Double-click `ButtonAndLed_OnOff.py`.
4. Click **Run current script**.
5. Press the button — LED toggles ON/OFF with each press.

---

## Code Explanation

### Toggle function
```python
def reverseGPIO():
    if led.value():
        led.value(0)
    else:
        led.value(1)
```
Reads the current LED state and sets it to the opposite — ON becomes OFF, OFF becomes ON.

### Button class and debounce

`Button` (in `button.py`) sets up the pin with the internal pull-up and registers an interrupt that calls `button_handler` when the pin goes from LOW to HIGH (button released):

```python
self.button.irq(trigger=Pin.IRQ_RISING, handler=self.button_handler)
```

`button_handler` ignores any trigger that happens within 200ms of the last accepted one, so contact bounce does not cause multiple toggles:

```python
def button_handler(self, pin):
    current_time = time.ticks_ms()
    delta_time = time.ticks_diff(current_time, self.last_press_time)
    if delta_time > 200:
        self.callback()
        self.last_press_time = current_time
```

The callback (`reverseGPIO`) therefore runs once per press, not continuously.

---

## Key Concepts

- **Debouncing**: ignoring the brief noise when a button transitions state (here by ignoring triggers within 200ms)
- **Toggle pattern**: reading current state and setting its inverse
- **Defining functions** with `def` in MicroPython
- **Interrupts**: the button triggers the callback without the main program having to poll it

## Further Exploration

- Rename the `reverseGPIO` button to something more descriptive.  For example `toggleLED`.

[Back to Module](./index.md)

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) Project 2.2
