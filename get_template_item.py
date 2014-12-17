from pyzabbix import zabbixapi
import json
url="http://10.210.71.145/zabbix/api_jsonrpc.php"
zb=zabbixapi(url=url,user="admin",password="zabbix")
response=zb.template.get({"output":"extend","filter": {"host": ["Template_webpress_ngxacc_status"]}})
templateid=json.loads(response.text)["result"][0]["templateid"]
params={"output": "extend","hostids":templateid}
response=zb.item.get(params)
item_list=json.loads(response.text)["result"]
for item in item_list:
    print item["key_"]
