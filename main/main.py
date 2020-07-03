from ota_update.main.ota_updater import OTAUpdater
import machine
import utime

pin2 = machine.Pin(2, machine.Pin.OUT)
def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/abhibhatia98/ESP-OTA-UPDATER')
    o.download_and_install_update_if_available('MOTO', '12345678')


def start():
    pin2.value(1)
     


def boot():
    download_and_install_update_if_available()
    start()


 boot()