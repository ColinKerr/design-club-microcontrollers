# Resistive Soil Moisture Sensor

Measure how wet soil is with a resistive soil moisture sensor and show the result as a percentage. This is a basic connection example: wire the sensor, read it, and calibrate it.

## New Concepts

- Resistive sensor
- Analog input (ADC)
- Calibration

### Resistive sensor

The two prongs of the probe act as a resistor in the soil. Wet soil conducts electricity better than dry soil, so the resistance between the prongs drops when the soil is wet. The module turns this into a voltage on its **AO** pin. On most modules of this type, wetter soil gives a lower voltage.

> **Note:** Current flows through the soil while the sensor is on. This slowly corrodes the probe. The probe in this kit has a corrosion-resistant coating, but it still wears out. See Further Exploration for a way to reduce this.

## Component List

![Components](../images/01_08_components.png)

The kit contains the ESP32-S3 board, the sensor module, a probe with cable, and jumper wires.

## Circuit

### Wiring Diagram

> Disconnect all power before building the circuit. Reconnect once verified.

![Wiring Diagram](../images/01_08_wiring_diagram.png)

**Connections:**
- Sensor `VCC` (+) → ESP32-S3 `3V3`
- Sensor `GND` (-) → ESP32-S3 `GND`
- Sensor `AO` → GPIO4

> **Warning:** Do not connect power in reverse. The chip burns out.

### Schematic Diagram

![Schematic Diagram](../images/01_08_schematic_diagram.png)

## Code

**Files:** [`01_first_examples/code/Soil_Moisture_Resistive.py`](./code/Soil_Moisture_Resistive.py), [`01_first_examples/code/soil_moisture.py`](./code/soil_moisture.py)

```python
from soil_moisture import SoilMoisture
import time

soil = SoilMoisture(4, dry=50000, wet=20000)

while True:
    print("Raw:", soil.raw, "Moisture:", soil.percent, "%")
    time.sleep(1)
```

## How to Run

### Online
1. Open Thonny → `01_first_examples/code/`.
2. Right-click `soil_moisture.py` → **Upload to /** if it isn't already on the device.
3. Double-click `Soil_Moisture_Resistive.py`.
4. Click **Run current script**.
5. Watch the shell. The sensor prints a raw value and a moisture percentage once per second.

### Calibrate the sensor

The values `dry=50000` and `wet=20000` are only guesses. Each sensor gives different readings. Follow these steps to find yours:

1. Hold the sensor in dry air. Write down the `Raw` value.
2. Put the sensor in a glass of water, up to the line on the probe. Write down the `Raw` value.
3. Change `dry` and `wet` in the code to your two values.
4. Run the program again. The percentage is now 0 in dry air and 100 in water.

---

## Code Explanation

### Create the sensor

```python
soil = SoilMoisture(4, dry=50000, wet=20000)
```
`SoilMoisture` reads the analog output of the sensor on GPIO4. The `dry` and `wet` values tell it which raw readings mean 0% and 100%.

### Read the sensor

```python
soil.raw
soil.percent
```
`raw` is the average of 10 readings of the analog-to-digital converter (ADC). The ADC turns the sensor voltage into a number from 0 to 65535. `percent` converts that number to a value from 0 to 100 using `dry` and `wet`.

### Why 3.3V power?

The module works from 3.3 V to 12 V. The analog output can not go above the supply voltage. The ESP32-S3 ADC accepts 3.3 V at most, so power the module from `3V3`.

---

## Key Concepts

- **Analog input**: the ADC measures a voltage, not just HIGH or LOW. See [ADC on ESP32-S3](../reference/ADC_on_ESP32_S3.md).
- **Calibration**: you measure two known points (dry and wet) so that readings become meaningful percentages.
- **Averaging**: the class averages 10 readings to reduce noise.
- **Reusable class**: `SoilMoisture` hides the ADC details behind `raw` and `percent`. The same class works for all soil sensors in this module.

See [Resistive Soil Moisture Sensor](../reference/Resistive_Soil_Moisture_Sensor.md) for the sensor details and [Class SoilMoisture](../reference/Class_SoilMoisture.md) for the library reference.

## Further Exploration

- Connect the **DO** pin to GPIO7 and read it with `Pin(7, Pin.IN)`. It goes LOW when the soil is wetter than the threshold set with the blue potentiometer.
- Power the sensor from a GPIO pin with `SoilMoisture(4, power_pin=8)` so it is on only while measuring. Check that the sensor takes less than 20 mA first.
- Turn on an LED when the soil is too dry.

[Back to Module](./index.md)
