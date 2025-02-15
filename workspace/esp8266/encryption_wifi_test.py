import os
import time

ssid_pw = b"PY96u8\xb2\xa6 \xbaw\xc8\xa4}]\x8c?\xe4'J\x83\t\xa70\x9b\xd64b\x15\xd7\x17\xd2"
decrypted_padded = cipher.decrypt(ssid_pw)
decrypted = unpad_message(decrypted_padded)

try:
    SSID, PASSWORD = decrypted.decode().split(" ")[:2]
except Exception as e:
    raise e


def connect_and_show_wifi_status():
    wlan.connect(SSID, PASSWORD)
    for _ in range(10):  # Try for ~5 seconds
        if wlan.isconnected():
            break
        time.sleep(0.5)
    print(wlan.ifconfig())


if __name__ == "__main__":
    connect_and_show_wifi_status()
