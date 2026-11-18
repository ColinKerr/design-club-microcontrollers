# Class RFID

Before each use of **RFID**, make sure `rfid.py` and `mfrc522.py` have been uploaded to `/` on the ESP32-S3, and then add the statement `from rfid import RFID` to the top of the Python file.

- **`RFID(sck, mosi, miso, cs, rst)`**: Creates the reader object and checks that the RC522 answers. Raises `RuntimeError` if it does not.
  - `sck`, `mosi`, `miso`: SPI GPIO numbers.
  - `cs`: GPIO number connected to the SDA pin of the board.
  - `rst`: GPIO number connected to the RST pin.
- **`read()`**: Returns `(uid, card_type)` when a tag is near the reader, otherwise `None`.
  - `uid`: Text such as `"04:A1:B2:C3"`. Tags have 4-byte or 7-byte UIDs.
  - `card_type`: Text such as `"MIFARE Classic 1K"`.

`mfrc522.py` is the low-level chip driver. It is based on [wendlers/micropython-mfrc522](https://github.com/wendlers/micropython-mfrc522) (MIT licence) with changes for the ESP32-S3.

> Copies of these modules can be found in [01_first_examples/code](../01_first_examples/code/).
