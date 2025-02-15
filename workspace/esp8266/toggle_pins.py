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

def set_pwm():
    # Initialize PWM on GPIO0
    pwm0 = PWM(Pin(2))  # Create PWM instance on pin 0
    pwm0.freq(60)  # Set frequency to 1 kHz
    pwm0.duty(1022)


if __name__ == '__main__':
    p = Pin(2, Pin.OUT)

    set_pwm()

    # set_pwm()
    time.sleep(3)
