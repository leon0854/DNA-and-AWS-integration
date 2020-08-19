import requests
import json
from requests.auth import HTTPBasicAuth
from get_token import get_token

def get_site_list(event, context):
    site_type = {'type' : 'building'}
    requests.packages.urllib3.disable_warnings()
    url = "https://10.10.1.2/dna/intent/api/v1/site"
    hdr = {'x-auth-token':get_token(event, context), 'content-type':'application/json'}
    resp = requests.get(url, headers=hdr, params=site_type, verify=False)
    site_list = resp.json()
    return site_list