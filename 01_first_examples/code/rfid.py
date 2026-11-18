from mfrc522 import MFRC522


class RFID:
    """Reads the unique ID (UID) and type of 13.56 MHz RFID / NFC cards with an RC522 board.

    Wire the board to the SPI pins you pass in. Use 3.3V power only.
    """

    # The SAK byte that every card sends tells us what family it belongs to.
    CARD_TYPES = {
        0x00: "MIFARE Ultralight / NTAG",
        0x08: "MIFARE Classic 1K",
        0x09: "MIFARE Mini",
        0x18: "MIFARE Classic 4K",
        0x20: "ISO 14443-4 (smart card)",
    }

    def __init__(self, sck, mosi, miso, cs, rst):
        self.reader = MFRC522(sck, mosi, miso, rst, cs)
        if self.reader.version() in (0x00, 0xFF):
            raise RuntimeError("RC522 not found. Check the wiring.")

    def read(self):
        """Returns (uid, card_type) when a card is near the reader, otherwise None.

        uid is text such as "04:A1:B2:C3". Call this in a loop to wait for a card.
        """
        status, _ = self.reader.request(MFRC522.REQIDL)
        if status != MFRC522.OK:
            return None

        uid = []
        for level in (0x93, 0x95):          # a 7-byte UID needs two rounds
            status, raw = self.reader.anticoll(level)
            if status != MFRC522.OK:
                return None
            if self.reader.select_tag(raw, level) != MFRC522.OK:
                return None
            if self.reader.sak & 0x04:      # UID is not complete yet
                uid += raw[1:4]             # raw[0] is a 0x88 marker, not part of the UID
            else:
                uid += raw[:4]
                break

        uid_text = ":".join("%02X" % byte for byte in uid)
        card_type = self.CARD_TYPES.get(self.reader.sak, "Unknown (SAK 0x%02X)" % self.reader.sak)
        return uid_text, card_type
