# Soil Moisture Sensor

Measure how wet soil is with a soil moisture sensor module and show the result as a percentage. This is a basic connection example: wire the sensor, read it, and calibrate it.

## New Concepts

- Soil moisture module
- Analog input (ADC)
- Calibration

### Soil moisture module

The module has a probe and a small board. The probe measures how wet the soil is. The board turns the result into a voltage on the **AO** pin. Some modules also have a **DO** pin that switches when the soil is wetter or drier than a threshold. This example uses only **AO**.

> **Note:** Check the type of your module in [Soil Moisture Sensor](../reference/Soil_Moisture_Sensor.md). Resistive probes corrode over time. Capacitive probes do not.

## Component List

![Components](../images/01_10_components.png)

The kit contains the ESP32-S3 board, the soil moisture module, and jumper wires.

## Circuit

### Wiring Diagram

> Disconnect all power before building the circuit. Reconnect once verified.

![Wiring Diagram](../images/01_10_wiring_diagram.png)

**Connections:**
- Sensor `VCC` → ESP32-S3 `3V3`
- Sensor `GND` → ESP32-S3 `GND`
- Sensor `AO` → GPIO6

> The product page for this sensor could not be checked while writing this page. If your board has different pin names or a different voltage range, see [Soil Moisture Sensor](../reference/Soil_Moisture_Sensor.md).

### Schematic Diagram

![Schematic Diagram](../images/01_10_schematic_diagram.png)

## Code

**Files:** [`01_first_examples/code/Soil_Moisture_Sensor.py`](./code/Soil_Moisture_Sensor.py), [`01_first_examples/code/soil_moisture.py`](./code/soil_moisture.py)

```python
from soil_moisture import SoilMoisture
import time

soil = SoilMoisture(6, dry=50000, wet=20000)

while True:
    print("Raw:", soil.raw, "Moisture:", soil.percent, "%")
    time.sleep(1)
```

## How to Run

### Online
1. Open Thonny → `01_first_examples/code/`.
2. Right-click `soil_moisture.py` → **Upload to /** if it isn't already on the device.
3. Double-click `Soil_Moisture_Sensor.py`.
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
soil = SoilMoisture(6, dry=50000, wet=20000)
```
`SoilMoisture` reads the analog output of the sensor on GPIO6. The `dry` and `wet` values tell it which raw readings mean 0% and 100%.

### Read the sensor

```python
soil.raw
soil.percent
```
`raw` is the average of 10 readings of the analog-to-digital converter (ADC). The ADC turns the sensor voltage into a number from 0 to 65535. `percent` converts that number to a value from 0 to 100 using `dry` and `wet`.

### Same class, different sensor

This example uses the same `SoilMoisture` class as the other two soil examples. Only the pin number changes. A class that does not depend on one specific sensor is easy to reuse.

---

## Key Concepts

- **Analog input**: the ADC measures a voltage, not just HIGH or LOW. See [ADC on ESP32-S3](../reference/ADC_on_ESP32_S3.md).
- **Calibration**: you measure two known points (dry and wet) so that readings become meaningful percentages.
- **Averaging**: the class averages 10 readings to reduce noise.
- **Reusable class**: `SoilMoisture` hides the ADC details behind `raw` and `percent`. The same class works for all soil sensors in this module.

See [Soil Moisture Sensor](../reference/Soil_Moisture_Sensor.md) for the sensor details and [Class SoilMoisture](../reference/Class_SoilMoisture.md) for the library reference.

## Further Exploration

- Use the [resistive](./01_08_resistive_soil_moisture.md), [capacitive](./01_09_capacitive_soil_sensor.md) and this sensor at the same time on GPIO4, GPIO5 and GPIO6. Do they agree?
- Turn on an LED when the soil is too dry.

[Back to Module](./index.md)
