import requests
import json
import pprint
from requests.auth import HTTPBasicAuth

def get_device(event, context):

    requests.packages.urllib3.disable_warnings()
    url="https://10.10.0.2/dataservice/device"
    resp=requests.get(url, auth=HTTPBasicAuth(username="admin", password ="C1sco@123"), verify=False)
    device_list = resp.json()["data"]
    pprint.pprint(device_list)
    return device_list



