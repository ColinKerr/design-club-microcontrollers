# Button and LED On and Off Switch


Toggle an LED on and off with a push button — press once to turn ON, press again to turn OFF. Unlike Project 2.1, the LED state persists after releasing the button. 

Uses the same components and circuit as Project 3

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



## Component List & Circuit Diagram

*Circuit and components are identical to Project 1.3*

## Code

**File:** [`01_first_examples/code/ButtonAndLed_OnOff.py`](./code/ButtonAndLed_OnOff.py)

```python
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

### Debounce logic
```python
if not button.value():        # 1. initial press detected
    time.sleep_ms(20)         # 2. wait 20ms
    if not button.value():    # 3. confirm still pressed
        reverseGPIO()         # 4. toggle
        while not button.value():  # 5. wait until released
            time.sleep_ms(20)
```

Step 5 prevents the LED from toggling again while the button is held down — the action fires once per press, not continuously.

---

## Key Concepts

- **Debouncing**: ignoring the brief noise when a button transitions state
- **Toggle pattern**: reading current state and setting its inverse
- **Defining functions** with `def` in MicroPython
- **Waiting for release**: important to avoid registering a single press as multiple events

## Further Exploration

- Rename the `reverseGPIO` button to something more descriptive.  For example `toggleLED`.

[Back to Module](./index.md)

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) Project 2.2
