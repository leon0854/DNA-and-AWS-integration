import requests
import json
from requests.auth import HTTPBasicAuth
from get_token import get_token

def get_device_list(event, context):
    requests.packages.urllib3.disable_warnings()
    url = "https://10.10.1.2/api/v1/network-device"
    hdr = {'x-auth-token':get_token(event, context), 'content-type':'application/json'}
    resp = requests.get(url,headers=hdr,verify=False)
    device_list = resp.json()
    return device_list