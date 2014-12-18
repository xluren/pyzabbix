from pyzabbix import zabbixapi
import json
url="http://10.210.71.145/zabbix/api_jsonrpc.php"
zb=zabbixapi(url=url,user="admin",password="zabbix")
response=zb.host.get(
        {
            "output":"interfaceid",
            "filter": 
            {
                "host":"all-summary"
            },
            "selectInterfaces":["interfaceid"]
        })
print json.dumps(json.loads(response.text),indent=2)
interfaceid=json.loads(response.text)["result"][0]["interfaces"][0]["interfaceid"]
print interfaceid
