import requests
import json
import pprint
from requests.auth import HTTPBasicAuth

def get_Tunnel_Health(event, context):

    requests.packages.urllib3.disable_warnings()
    url="https://10.10.0.2:8443/dataservice/statistics/approute/tunnels/summary/latency?limit=10"
    resp=requests.get(url, auth=HTTPBasicAuth(username="admin", password ="C1sco@123"), verify=False)
    Tunnel_Health = resp.json()["data"]
    pprint.pprint(Tunnel_Health)
    return Tunnel_Health





