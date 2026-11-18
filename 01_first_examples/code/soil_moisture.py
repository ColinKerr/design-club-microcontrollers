from machine import ADC, Pin
import time


class SoilMoisture:
    """Reads an analog soil moisture sensor and converts it to a percentage.

    pin       -- GPIO number connected to the sensor's analog output (use GPIO 1-10, they are ADC1)
    dry, wet  -- raw readings (0-65535) in dry air and in water, see calibrate_dry() / calibrate_wet()
    power_pin -- optional GPIO that powers the sensor, so it is only on while measuring
    """

    def __init__(self, pin, dry=50000, wet=20000, power_pin=None):
        self.adc = ADC(Pin(pin))
        self.adc.atten(ADC.ATTN_11DB)      # measure the full 0 - 3.3V range
        self.dry = dry
        self.wet = wet
        self.power = None
        if power_pin is not None:
            self.power = Pin(power_pin, Pin.OUT, value=0)

    @property
    def raw(self):
        """Average of 10 readings, 0 - 65535. Averaging smooths out noise."""
        if self.power:
            self.power.value(1)
            time.sleep_ms(20)              # let the sensor settle
        total = 0
        for _ in range(10):
            total += self.adc.read_u16()
        if self.power:
            self.power.value(0)
        return total // 10

    @property
    def percent(self):
        """Moisture from 0 (as dry as the dry value) to 100 (as wet as the wet value)."""
        if self.dry == self.wet:
            return 0
        value = (self.raw - self.dry) * 100 // (self.wet - self.dry)
        return max(0, min(100, value))

    def calibrate_dry(self):
        """Call with the sensor in dry air. Stores and returns the dry value."""
        self.dry = self.raw
        return self.dry

    def calibrate_wet(self):
        """Call with the sensor in water (up to the line). Stores and returns the wet value."""
        self.wet = self.raw
        return self.wet
