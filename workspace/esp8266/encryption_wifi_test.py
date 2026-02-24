import os
import time
from machine import Pin, PWM


def decrypt_message(message):
    decrypted_padded = cipher.decrypt(message)
    return unpad_message(decrypted_padded).decode()


SSID_ENCRYPTED = b"\x08A\xe2@\x9cDy\xab\xde\x1cVFV0\xcd\xc8\xb7\x19\xf6\x8c(oL\x14\x08|\x89eg\xe77\xb7"
PASSWORD_ENCRYPTED = (
    b"\xe0\xad;\x1a\x89\xd7\xae\xf2\xa9\xa8\xd2^\x04\x8e\x02\xae\x05Q<\x95\xe5\x97\x96l\xeaU\xee\xab\x85-no"
)


try:
    SSID = decrypt_message(SSID_ENCRYPTED)
    PASSWORD = decrypt_message(PASSWORD_ENCRYPTED)
except Exception as e:
    raise e


def enable_led():
    # Initialize PWM on GPIO0
    pwm0 = PWM(Pin(2))  # Create PWM instance on pin 2
    pwm0.freq(500)
    pwm0.duty(1000)


def connect_and_show_wifi_status():
    print(f"trying to connect to {SSID} with password={PASSWORD}")
    wlan.connect(SSID, PASSWORD)
    for _ in range(20):  # Try for ~5 seconds
        if wlan.isconnected():
            enable_led()
            break
        time.sleep(0.5)
        print("trying to connect with wifi")

    print(f"Connected!! IP ADDRESS = {wlan.ifconfig()[0]}")


if __name__ == "__main__":
    p = Pin(2, Pin.OUT)
    p.value(0)
    connect_and_show_wifi_status()
