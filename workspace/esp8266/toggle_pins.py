# start with checking if there is wifi avaible?

import time

from machine import Pin, PWM


def set_pin_low(pin_no):
    p0 = Pin(pin_no, Pin.OUT)
    p0.off()
    print(f"A{pin_no} was set to low")

def set_pin_high(pin_no):
    p0 = Pin(pin_no, Pin.OUT)
    p0.on()
    print(f"A{pin_no} was set to high")


if __name__ == '__main__':
    p = Pin(0, Pin.OUT)
    p.value(0)
    time.sleep(3)
