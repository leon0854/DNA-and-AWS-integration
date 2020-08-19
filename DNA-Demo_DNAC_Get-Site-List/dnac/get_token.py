import requests
from requests.auth import HTTPBasicAuth
import json

def get_token(event, context):
    username = "admin"
    password = "C1sco@123"
    requests.packages.urllib3.disable_warnings()
    url = "https://10.10.1.2/dna/system/api/v1/auth/token"
    resp = requests.post(url, auth=HTTPBasicAuth(username, password), verify=False)
    token = resp.json()["Token"]
    return token