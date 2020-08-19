import json
import re
from get_device_list import get_device_list

def get_serial_no(event, context):
    str_device_list = str(get_device_list(event, context))
    find_serial_no = re.findall(r"'serialNumber': '(.*?)', 'hostname'", str_device_list, re.S)
    return find_serial_no