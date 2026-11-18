# Resistive Soil Moisture Sensor

A resistive soil moisture sensor measures how well the soil conducts electricity. Wet soil conducts better than dry soil. The module turns this into an analog voltage and a digital signal.

**Source:** ICStation Resistive Soil Moisture Sensor with Corrosion Resistant Probe (Amazon ASIN B076DDWDJK). The values below come from the manufacturer's sheet: [Resistive_Soil_Moisture_Sensor.pdf](./Resistive_Soil_Moisture_Sensor.pdf).

## Specifications

| Item | Value |
|-|-|
| Working voltage | 3.3 V to 12 V DC |
| Working current | less than 20 mA |
| Output current | less than 30 mA (DO output about 10 mA) |
| Board size | 36 x 15 x 6 mm |
| Probe length | 8.8 cm |
| Probe pin pitch | 5 mm |
| Probe cable length | 1.2 m |
| Probe connector | XH2.54 2-pin |
| Probe material | Corrosion-resistant alloy, rated for at least 6 months in soil |

## Pins

| Pin | Description |
|-|-|
| + (VCC) | Power. Connect to 3.3 V on the ESP32-S3 so the analog output stays within the ADC range. |
| - (GND) | Ground. |
| DO | Digital output. Goes LOW when the moisture passes the threshold set with the blue potentiometer. |
| AO | Analog output. The voltage changes with moisture. |

> **Warning:** Do not connect power in reverse. The chip burns out.

## Indicator LEDs and threshold

- The **P** LED is on when the module has power.
- The **S** LED shows the state of the digital signal.
- Turn the blue potentiometer clockwise to raise the detection threshold, and counter-clockwise to lower it.
- If the **S** LED stays on at either end of the turn, the threshold is out of range.
- The potentiometer changes only the **DO** output. It does not change the **AO** output.

## Notes

- **More moisture gives a lower AO voltage on most modules of this type.** Measure your own module in dry air and in water to confirm.
- Current flowing through the probe corrodes it over time. Power the module only when you measure, if you can.

See [Class SoilMoisture](./Class_SoilMoisture.md) for the library used in the examples.
