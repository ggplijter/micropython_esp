import os
import time
from machine import Pin, PWM

ssid_pw = b"PY96u8\xb2\xa6 \xbaw\xc8\xa4}]\x8c?\xe4'J\x83\t\xa70\x9b\xd64b\x15\xd7\x17\xd2"
decrypted_padded = cipher.decrypt(ssid_pw)
decrypted = unpad_message(decrypted_padded)

try:
    SSID, PASSWORD = decrypted.decode().split(" ")[:2]
except Exception as e:
    raise e

def enable_led():
    # Initialize PWM on GPIO0
    pwm0 = PWM(Pin(2))  # Create PWM instance on pin 0
    pwm0.freq(5)  # Set frequency to 1 kHz
    pwm0.duty(500)

def connect_and_show_wifi_status():
    wlan.connect(SSID, PASSWORD)
    for _ in range(10):  # Try for ~5 seconds
        if wlan.isconnected():
            enable_led()
            break
        time.sleep(0.5)
    print(wlan.ifconfig())



if __name__ == "__main__":
    p = Pin(2, Pin.OUT)
    p.value(1)
    connect_and_show_wifi_status()
