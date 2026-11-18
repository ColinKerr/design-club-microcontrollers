# Capacitive Soil Sensor

Measure how wet soil is with a capacitive soil sensor and show the result as a percentage. This is a basic connection example: wire the sensor, read it, and calibrate it.

## New Concepts

- Capacitive sensor
- Analog input (ADC)
- Calibration

### Capacitive sensor

A capacitive sensor has no bare metal in the soil. Two copper areas under a coating form a capacitor. Water in the soil changes the dielectric constant around the capacitor, and with it the charge the capacitor holds. The electronics on the board turn this into a voltage on the **AOUT** pin. The voltage is between 0 V and 3.0 V, so the ESP32-S3 can read it directly. On most boards of this type, wetter soil gives a lower voltage. You find out how yours behaves when you calibrate it.

Because nothing touches the soil, the sensor does not corrode like a resistive sensor.

> **Note:** Put the sensor in the soil only up to the line on the board. The electronics above the line must stay dry.

## Component List

![Components](../images/01_09_components.png)

The kit contains the ESP32-S3 board, a capacitive sensor and its 3-pin wire (PH2.54 connector). The sensor is 98 x 23 mm.

## Circuit

### Wiring Diagram

> Disconnect all power before building the circuit. Reconnect once verified.

![Wiring Diagram](../images/01_09_wiring_diagram.png)

**Connections:**
- Sensor `VCC` → ESP32-S3 `3V3`
- Sensor `GND` → ESP32-S3 `GND`
- Sensor `AOUT` → GPIO5

The included 3-pin wire plugs into the sensor. Connect its other end to the ESP32-S3 with jumper pins.

### Schematic Diagram

![Schematic Diagram](../images/01_09_schematic_diagram.png)

## Code

**Files:** [`01_first_examples/code/Soil_Moisture_Capacitive.py`](./code/Soil_Moisture_Capacitive.py), [`01_first_examples/code/soil_moisture.py`](./code/soil_moisture.py)

```python
from soil_moisture import SoilMoisture
import time

soil = SoilMoisture(5, dry=50000, wet=20000)

while True:
    print("Raw:", soil.raw, "Moisture:", soil.percent, "%")
    time.sleep(1)
```

## How to Run

### Online
1. Open Thonny → `01_first_examples/code/`.
2. Right-click `soil_moisture.py` → **Upload to /** if it isn't already on the device.
3. Double-click `Soil_Moisture_Capacitive.py`.
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
soil = SoilMoisture(5, dry=50000, wet=20000)
```
`SoilMoisture` reads the analog output of the sensor on GPIO5. The `dry` and `wet` values tell it which raw readings mean 0% and 100%.

### Read the sensor

```python
soil.raw
soil.percent
```
`raw` is the average of 10 readings of the analog-to-digital converter (ADC). The ADC turns the sensor voltage into a number from 0 to 65535. `percent` converts that number to a value from 0 to 100 using `dry` and `wet`.

### Compare with the resistive sensor

The readings of a capacitive sensor change more smoothly and drift less over time. Try both sensors in the same pot and compare their `percent` values.

---

## Key Concepts

- **Analog input**: the ADC measures a voltage, not just HIGH or LOW. See [ADC on ESP32-S3](../reference/ADC_on_ESP32_S3.md).
- **Calibration**: you measure two known points (dry and wet) so that readings become meaningful percentages.
- **Averaging**: the class averages 10 readings to reduce noise.
- **Reusable class**: `SoilMoisture` hides the ADC details behind `raw` and `percent`. The same class works for all soil sensors in this module.

See [Capacitive Soil Moisture Sensor](../reference/Capacitive_Soil_Sensor.md) for the sensor details and [Class SoilMoisture](../reference/Class_SoilMoisture.md) for the library reference.

## Further Exploration

- Compare this sensor with the [resistive sensor](./01_08_resistive_soil_moisture.md) in the same pot. Which one is more stable?
- Print one reading per minute and record the values for a day. How does the soil dry out?
- Turn on an LED when the soil is too dry.

[Back to Module](./index.md)
