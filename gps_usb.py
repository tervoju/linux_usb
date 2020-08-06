
from usb_port import list_devices

GPS_DEVICE_VENDOR = '1546'
GPS_DEVICE_ID = '01a8'

GPS_PORTS = list_devices(GPS_DEVICE_VENDOR, GPS_DEVICE_ID)

if GPS_PORTS != []:
    print(GPS_PORTS)
    print(GPS_PORTS[0])


