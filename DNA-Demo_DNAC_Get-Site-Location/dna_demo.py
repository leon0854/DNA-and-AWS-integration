import requests
import socket
import json
from requests.auth import HTTPBasicAuth
from get_token import get_token
from get_site_id import get_site_id

def tcp_socket(event, context):
    n = 0
    
    for site in get_site_id(event, context):
        site_id = {"siteId": "%s" % get_site_id(event, context)[n]}
        n = n+1
        
        def get_site_location():
            requests.packages.urllib3.disable_warnings()
            url = "https://10.10.1.2/dna/intent/api/v1/site"
            hdr = {'x-auth-token': get_token(event, context), 'content-type': 'application/json'}
            resp = requests.get(url, headers=hdr, params=site_id, verify=False)
            site_location = resp.json()
            return site_location
            
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('10.11.2.7', 7006))
            s.send(str(json.dumps(get_site_location())).encode('utf-8'))
            s.close()
