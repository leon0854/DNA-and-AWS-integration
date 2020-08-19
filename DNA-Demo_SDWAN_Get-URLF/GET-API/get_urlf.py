import requests
import json
import pprint
from get_token_cookie import create_secHeder
from requests.auth import HTTPBasicAuth

def get_urlf(event, context):
    token_cookie=create_secHeder(event, context)
    token=token_cookie['Content-Type']
    cooki=token_cookie['Cookie']

    requests.packages.urllib3.disable_warnings()
    url = "https://10.10.0.2:443/dataservice/statistics/urlf?api_key=url&last_24_hours=Last 24 hours"
    hdr = {'X-XSRF-TOKEN':token, 'content-type': 'application/json','Cookie':cooki}
    resp = requests.get(url, headers=hdr, auth=HTTPBasicAuth(username="admin", password="C1sco@123"), verify=False)
    urlf = resp.json()["data"]
    pprint.pprint(urlf)
    return urlf

