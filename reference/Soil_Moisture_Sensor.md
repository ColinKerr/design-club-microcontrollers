# Soil Moisture Sensor (generic module)

This page describes a soil moisture module with an LM393 comparator and both analog and digital outputs.

**Source:** Product name from `GOAL.md`: "Soil Moisture Sensor Module, LM393, Analog Digital" (Amazon ASIN B0FX2PRYFS).

An LM393 is a comparator chip. It makes the digital **DO** output from the analog voltage and a threshold that you set with a potentiometer. The module therefore has both an analog output (**AO**) and a digital output (**DO**).

> **Verify before use:** The product page could not be read automatically. The specifications below are typical for modules with an LM393 and an analog and a digital output. Check them against the text printed on your board.

## Typical specifications

| Item | Typical value |
|-|-|
| Working voltage | 3.3 V to 5 V DC |
| Outputs | AO (analog voltage) and DO (digital, from the LM393 comparator) |
| Interface | 4 pins: VCC, GND, AO, DO |

## Pins

| Pin | Description |
|-|-|
| VCC | Power. Use 3.3 V with the ESP32-S3. |
| GND | Ground. |
| AO | Analog output. Connect to an ADC pin. |
| DO | Digital output. Changes state at the threshold set by the potentiometer. |

## Notes

- **More moisture usually gives a lower AO voltage.** Measure your own module in dry air and in water to confirm.
- A resistive probe corrodes over time. Power the module only when you measure, if you can.
- Do not power the module from 5 V if you connect AO straight to the ESP32-S3. The ADC pin accepts 3.3 V at most.

See [Class SoilMoisture](./Class_SoilMoisture.md) for the library used in the examples.
