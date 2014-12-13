import requests
import json 
class zabbixapi(object):
    def __init__(self,url,user,password,headers={"Content-Type":"application/json"}):
        self.request_data={
            "jsonrpc":"2.0",
            "method":"user.login",
            "params":"null",
            "id": 1,
            "auth":""
        }
        self.url=url
        self.headers=headers
        self.login(user,password)

    def login(self,user,password):
        method="user.login"
        params={"user":user,"password":password}
        response=self.deal_request(method=method,params=params)
        auth=json.loads(response.text)["result"]
        print auth
        self.request_data["auth"]=auth

    def deal_request(self,method,params):
        self.request_data["method"]=method
        self.request_data["params"]=params
        response=requests.post(url=self.url,data=json.dumps(self.request_data),headers=self.headers)
        return response
    def __getattr__(self,name):
        return zabbixobj(name,self)

class zabbixobj(object):
    def __init__(self,method_fomer,zabbixapi):
        self.method_fomer=method_fomer
        self.zabbixapi=zabbixapi

    def __getattr__(self, name):
        def func(params):
            method=self.method_fomer+"."+name
            params=params
            return  self.zabbixapi.deal_request(method=method,params=params)
        return func

