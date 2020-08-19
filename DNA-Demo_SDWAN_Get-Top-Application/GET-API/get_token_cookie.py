import json
import requests
import pprint
from requests.auth import HTTPBasicAuth

def create_secHeder(event, context):
  res = requests.session()

  secHeaders = {}
  loginUrl = 'https://10.10.0.2/jts/authenticated/j_security_check'
  loginHeaders = {'Content-Type': 'application/x-www-form-urlencoded'}
  loginData = {'j_username' : "admin", 'j_password' : "C1sco@123"}

  login_response = res.post(loginUrl, data = loginData, headers = loginHeaders, verify=False)

  tokeSession = res.get('https://10.10.0.2:8443/dataservice/client/server', headers=None, verify=False)

  secHeaders['Cookie'] = login_response.headers['Set-Cookie'].split(';')[0]
  secHeaders['Content-Type'] = json.loads((tokeSession.content))['data']['CSRFToken']
  
  token_cookie= secHeaders
  return token_cookie

