import requests
import json
import pprint
from requests.auth import HTTPBasicAuth

def get_device_hardwarehealth(event, context):

    requests.packages.urllib3.disable_warnings()
    url="https://10.10.0.2:8443/dataservice/device/hardwarehealth/summary"
    resp=requests.get(url, auth=HTTPBasicAuth(username="admin", password ="C1sco@123"), verify=False)
    hardwarehealth = resp.json()["data"]
    pprint.pprint(hardwarehealth)
    return hardwarehealth



