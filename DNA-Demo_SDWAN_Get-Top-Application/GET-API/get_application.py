import requests
import json
import pprint
from get_token_cookie import create_secHeder
from requests.auth import HTTPBasicAuth

def get_application(event, context):
    
    token_cookie=create_secHeder(event, context)
    token=token_cookie['Content-Type']
    cooki=token_cookie['Cookie']

    requests.packages.urllib3.disable_warnings()
    url = "https://10.10.0.2:8443/dataservice/statistics/dpi/applications/summary"
    hdr = {'X-XSRF-TOKEN':token, 'content-type': 'application/json','Cookie':cooki}
    resp = requests.get(url, headers=hdr, auth=HTTPBasicAuth(username="admin", password="C1sco@123"), verify=False)
    application = resp.json()["data"]
    pprint.pprint(application)
    return application




