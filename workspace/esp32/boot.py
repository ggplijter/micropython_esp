# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)


DO_CONNECT_WIFI = True
DO_IMPORT_WEBREPL = True

if DO_IMPORT_WEBREPL:
    import webrepl
    webrepl.start()

if DO_CONNECT_WIFI:
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("SSID", "PASSWORD")
