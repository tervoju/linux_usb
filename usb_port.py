# inspiration from this github repo
# https://github.com/dhylands/usb-ser-mon
# how to get logical path to connected usb device based on vendor id and product id

import pyudev
import sys

def is_usb_serial(device, vid=None, pid=None):
    # Checks device to see if its a USB Serial device.
    # The caller already filters on the subsystem being 'tty'.
    # If serial_num or vendor is provided, then it will further check to
    # see if the serial number and vendor of the device also matches.

    # cannot be right if no vendor id
    if 'ID_VENDOR' not in device.properties:
        return False
    # searcing for right vendor
    if vid is not None:
        if device.properties['ID_VENDOR_ID'] != vid:
            print(vid + ' not found  ' + device.properties['ID_VENDOR_ID'])
            return False

    if pid is not None:
        if device.properties['ID_MODEL_ID'] != pid:
            print('not found')
            return False
    return True

def list_devices(vid=None, pid=None):
    devs = []
    context = pyudev.Context()
    for device in context.list_devices(subsystem='tty'):
        if is_usb_serial(device, vid= vid,  pid = pid):
            devs.append(device.device_node)
    return devs