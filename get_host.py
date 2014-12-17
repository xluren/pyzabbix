from pyzabbix import zabbixapi
import json
url="http://10.210.71.145/zabbix/api_jsonrpc.php"
#log in 
zb=zabbixapi(url=url,user="admin",password="zabbix")
response=zb.host.get(
        {
            "output":"extend",
            "filter": 
            {
                "host":"all-summary"
            }
        })
print json.dumps(json.loads(response.text),indent=2)

response=zb.host.get({"output": ["extend","hostid"],"filter": {"host": ["all-summary"]}})
print json.dumps(json.loads(response.text),indent=2)
