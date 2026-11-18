from soil_moisture import SoilMoisture
import time

# Analog output (AOUT) on GPIO5. Replace dry and wet with your own readings.
soil = SoilMoisture(5, dry=50000, wet=25000)

while True:
    print("Raw:", soil.raw, "Moisture:", soil.percent, "%")
    time.sleep(1)
