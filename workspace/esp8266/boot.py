# This file is executed on every boot (including wake-boot from deepsleep)
import os

import esp
import machine
import ucryptolib

esp.osdebug(None)

DO_CONNECT_WIFI = True
DO_IMPORT_WEBREPL = False

if DO_IMPORT_WEBREPL:
    import webrepl
    webrepl.start()

if DO_CONNECT_WIFI:
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

def pad_message(msg):
    pad_length = 16 - (len(msg) % 16)
    return msg + bytes([pad_length] * pad_length)

def unpad_message(msg):
    pad_length = msg[-1]
    return msg[:-pad_length]

key = pad_message(os.uname().version.encode('utf-8'))[:16]
iv = pad_message(os.uname().release.encode('utf-8'))[:16]

cipher = ucryptolib.aes(key, 2, iv)

gc.collect()