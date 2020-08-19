import requests
import json
from requests.auth import HTTPBasicAuth
from get_token import get_token

def get_network_health(event, context):
    requests.packages.urllib3.disable_warnings()
    url="https://10.10.1.2/dna/intent/api/v1/network-health"
    hdr = {'x-auth-token':get_token(event, context), 'content-type':'application/json'}
    resp=requests.get(url,headers=hdr,verify=False)
    network_health=resp.json()
    return network_health