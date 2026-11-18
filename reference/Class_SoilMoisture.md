# Class SoilMoisture

Before each use of **SoilMoisture**, make sure `soil_moisture.py` has been uploaded to `/` on the ESP32-S3, and then add the statement `from soil_moisture import SoilMoisture` to the top of the Python file.

- **`SoilMoisture(pin, dry=50000, wet=20000, power_pin=None)`**: Creates the sensor object.
  - `pin`: GPIO number connected to the sensor's analog output. Use GPIO 1 to 10 (ADC1).
  - `dry`: Raw reading in dry air.
  - `wet`: Raw reading in water.
  - `power_pin`: Optional GPIO that powers the sensor. When set, the sensor is on only while it measures.
- **`raw`**: Average of 10 readings, from 0 to 65535.
- **`percent`**: Moisture from 0 to 100, calculated from `raw`, `dry` and `wet`.
- **`calibrate_dry()`**: Stores the current raw reading as `dry` and returns it.
- **`calibrate_wet()`**: Stores the current raw reading as `wet` and returns it.

> A copy of this module can be found here: [01_first_examples/code/soil_moisture.py](../01_first_examples/code/soil_moisture.py)
