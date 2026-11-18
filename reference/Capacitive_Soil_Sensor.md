# Capacitive Soil Moisture Sensor

A capacitive soil moisture sensor measures the **dielectric constant** of the soil, not its electrical conductivity. Water changes the dielectric constant strongly, so the sensor can tell wet soil from dry soil. The sensor has no exposed metal contacts. Moisture and minerals cannot corrode it, so the output stays stable over a long time.

**Source:** Amazon listing, ASIN B0F9WX5XH6 (10-piece kit).

## Specifications

| Item | Value |
|-|-|
| Operating voltage | 3.3 V DC |
| Output | Analog voltage, 0 to 3.0 V DC |
| Interface | PH2.54 3-pin connector: VCC, GND, AOUT |
| Size | 98 x 23 mm |
| Kit contents | 10 sensors and 10 connecting wires (3-pin) |

The output range of 0 to 3.0 V fits the ADC of the ESP32-S3 without extra parts.

## Pins

| Pin | Description |
|-|-|
| VCC | Power. Connect to 3.3 V. |
| GND | Ground. |
| AOUT | Analog output, 0 to 3.0 V. Connect to an ADC pin. |

The included wire plugs into the 3-pin connector. You do not need to solder.

## Notes

- The listing does not say whether wet soil gives a higher or a lower voltage. On most capacitive sensors of this type, wetter soil gives a **lower** voltage. Measure your own sensor in dry air and in water to find out.
- The readings have no unit. Convert them to a percentage with a dry and a wet calibration value.
- Keep the electronics on the board dry. Push the sensor into the soil only as deep as the printed line, if your board has one.
- The listing names Arduino and Raspberry Pi as compatible boards. A Raspberry Pi has no analog inputs, so it needs an extra ADC chip. The ESP32-S3 reads the sensor directly.

See [Class SoilMoisture](./Class_SoilMoisture.md) for the library used in the examples.
