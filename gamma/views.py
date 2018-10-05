from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuarios.models import Tran
from oic.oic.message import AuthorizationResponse
from oic import rndstr
from oic.utils.http_util import Redirect
import requests
import json
from collections import namedtuple
from oic.oic import Client
from oic.utils.authn.client import CLIENT_AUTHN_METHOD

def home(request):
    template_name = 'index.html'
    if 'code' in str(request):
        r = open("transactions.json")
        trans = json.loads(r.read(), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        req_pos = str(request).find('?')
        req = str(request)[req_pos + 1:].split('&')
        query = request.GET.get('code')
        data = {'grant_type':'authorization_code', 'scope':'openid',
                'code':query,
                'redirect_uri':'http://localhost:8000'}
        headers = { 'Content-Type':'application/x-www-form-urlencoded',
                    'Authorization':'Basic QCEyODE5LjQ2RjUuNEM5MC5BNkJBITAwMDEhNTNEOS43MTcwITAwMDghNEJENC5EQTk0LkZGOEUuNUY1RDpwYXNzd29yZA=='}
        res_token = requests.post("https://sso.trust.lat/oxauth/restv1/token", data=data, headers=headers)
        dicc_token = res_token.json()
        print(dicc_token)
        return render(request, template_name, {'trans':trans})
    else:
        return redirect('https://sso.trust.lat/oxauth/restv1/authorize?scope=openid&response_type=code&client_id=@!2819.46F5.4C90.A6BA!0001!53D9.7170!0008!4BD4.DA94.FF8E.5F5D&redirect_uri=http://localhost:8000')

def detalles(request):
    template_name = 'detalle.html'
    return render(request, template_name)

#Codigo utils
    # client = Client(client_authn_method=CLIENT_AUTHN_METHOD)
    # uid = "https://sso.trust.lat"
    # issuer = client.discover(uid)
    #r = requests.get('http://192.168.2.133:8050/api/transactions')
    # query = request.GET.get('code')
    # print (res_token['access_token'])
    #If you're in a WSGI environment
    # session={}
    # session["state"] = rndstr()
    # session["nonce"] = rndstr()
    # args = {
    #     "client_id": '@!35B7.97A9.DED0.1B74!0001!5223.01BA!0008!2BDA.EB86.0EA0.3C24',
    #     "response_type": "code",
    #     "scope": ["openid"],
    #     "nonce": session["nonce"],
    #     "redirect_uri": "http://localhost:8000",
    #     "state": session["state"]
    # }
    # auth_req = client.construct_AuthorizationRequest(request_args=args)
    # login_url = auth_req.request(client.authorization_endpoint)
    # return Redirect(login_url)
    # response = request["QUERY_STRING"]
    # aresp = client.parse_response(AuthorizationResponse, info=response, sformat="urlencoded")
    # code = aresp["code"]
    # assert aresp["state"] == session["state"]
    # print(code)
    # for valor in req:
    #     keyValue=valor.split("=")
    #     if len(keyValue) == 2:
    #         dicc[keyValue[0]]=keyValue[1]
    #     else:
    #         dicc[keyValue[0]]=None
