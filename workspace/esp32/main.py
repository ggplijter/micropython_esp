# start with checking if there is wifi avaible?

import time

from machine import Pin, PWM


def show_wifi_status():
    for _ in range(10):  # Try for ~5 seconds
            if wlan.isconnected():
                break
            time.sleep(0.5)
    print(wlan.ifconfig())


def set_pin_low(pin_no):
    p0 = Pin(pin_no, Pin.OUT)
    p0.off()
    print(f"A{pin_no} was set to low")

def set_pin_high(pin_no):
    p0 = Pin(pin_no, Pin.OUT)
    p0.on()
    print(f"A{pin_no} was set to high")


def set_pwm():
    # Initialize PWM on GPIO0
    pwm0 = PWM(Pin(0))  # Create PWM instance on pin 0
    pwm0.freq(25000)  # Set frequency to 1 kHz
    pwm0.duty(500)

    # set_pin_high(0)

    while True:
        pass


if __name__ == '__main__':
    p = Pin(0, Pin.OUT)
    p.value(0)

    show_wifi_status()
    # set_pin_high()
    # set_pwm()

    # set_pin_high(pin_no=2)
    # time.sleep(.2)
    set_pwm()
    # time.sleep(10)