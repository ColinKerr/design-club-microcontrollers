# RC522 RFID Reader

The RC522 module (also sold as MF522-AN) uses the NXP (formerly Philips) MFRC522 chip. It reads and writes 13.56 MHz RFID and NFC tags that follow ISO/IEC 14443 type A. It talks to the microcontroller over SPI.

**Sources:**
- Retailer description of the "RFID Module Kit - Mifare RC522 RF IC Card Sensor Module + S50 White Blank Card + Key Ring" (Amazon ASIN B0FND311F3). The kit may differ slightly from this description.
- The NFC 216 sticker listing (Amazon ASIN B0HHJPH3FY): the stickers follow the NTAG216 standard.
- NXP datasheets for the MFRC522 chip and the NTAG216 tag (for the memory and UID values).

## Specifications

| Item | Value |
|-|-|
| Chip | NXP MFRC522 |
| Frequency | 13.56 MHz |
| Working voltage | 3.3 V only. **Do not use 5 V.** |
| Interface | SPI |
| Operating current | 13 to 26 mA at 3.3 V |
| Idle current | 10 to 13 mA at 3.3 V |
| Sleep current | less than 80 µA |
| Peak current | less than 30 mA |
| Board size | 40 x 60 mm |
| Operating temperature | -20 to 80 °C |
| Storage temperature | -40 to 85 °C |
| Relative humidity | 5% to 95% |

## Supported tag types

The listing names these tag types: MIFARE Classic S50 (1K), MIFARE Classic S70 (4K), MIFARE Ultralight, MIFARE Pro and MIFARE DESFire. The chip also reads NTAG tags, such as the NTAG216 stickers.

The examples in this course read the UID and the type of any tag. They read and write the memory of MIFARE Classic 1K and NTAG tags. MIFARE Pro and DESFire need extra protocol steps that the examples do not implement.

## Pins

| Pin | Description |
|-|-|
| 3.3V | Power. 3.3 V only. |
| GND | Ground. |
| RST | Reset. LOW resets the chip. |
| SDA | SPI chip select (CS). On this board the pin is named SDA, but it is **not** an I2C pin. |
| SCK | SPI clock. |
| MOSI | SPI data from the microcontroller to the board. |
| MISO | SPI data from the board to the microcontroller. |
| IRQ | Interrupt output. Not used in the examples. |

## Tags

| Tag | Type | Memory | UID length |
|-|-|-|-|
| Card (S50 white blank card, in the kit) | MIFARE Classic 1K (S50) | 1 KB: 16 sectors of 4 blocks of 16 bytes | usually 4 bytes |
| Key ring (in the kit) | S50-type fob. The listing does not name the type, so check it with the reader. | usually 1 KB | usually 4 bytes |
| NFC 216 sticker (sold separately) | NTAG216 (NFC Forum Type 2) | 888 bytes of user memory | 7 bytes |

The **UID** is the unique ID of a tag. The reader finds the tag type from the **SAK** byte that the tag sends when it is selected:

| SAK | Tag family |
|-|-|
| `0x08` | MIFARE Classic 1K |
| `0x09` | MIFARE Mini |
| `0x18` | MIFARE Classic 4K |
| `0x00` | MIFARE Ultralight or NTAG |
| `0x20` | ISO 14443-4 smart card (for example MIFARE DESFire) |

## Version check

The chip version register returns `0x91` or `0x92` on genuine chips. Some clones return other values. A value of `0x00` or `0xFF` means that no chip answers, usually because of a wiring error.

See [Class RFID](./Class_RFID.md) for the library used in the examples.
