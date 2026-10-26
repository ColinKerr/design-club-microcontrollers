from button import Button
from machine import Pin

def reverseGPIO():
    if led.value():
        led.value(0)
    else:
        led.value(1)

led = Pin(2, Pin.OUT)

button = Button(13, reverseGPIO)