from soil_moisture import SoilMoisture
import time

# Analog output (AO) on GPIO4. Replace dry and wet with your own readings.
soil = SoilMoisture(4, dry=50000, wet=20000)

while True:
    print("Raw:", soil.raw, "Moisture:", soil.percent, "%")
    time.sleep(1)
