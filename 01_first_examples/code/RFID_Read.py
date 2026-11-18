from rfid import RFID
import time

reader = RFID(sck=4, mosi=5, miso=6, cs=7, rst=8)
print("Hold a card near the reader...")

last_uid = None
while True:
    card = reader.read()
    if card and card[0] != last_uid:
        uid, card_type = card
        print("UID:", uid, "Type:", card_type)
        last_uid = uid
    elif card is None:
        last_uid = None
    time.sleep_ms(200)
