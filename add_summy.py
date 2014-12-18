from pyzabbix import zabbixapi
import json
url="http://10.210.71.145/zabbix/api_jsonrpc.php"
zb=zabbixapi(url=url,user="admin",password="zabbix")
response=zb.host.get(
        {
            "output":["interfaceid","hostids"],
            "filter": 
            {
                "host":"all-summary"
            },
            "selectInterfaces":["interfaceid"]
        })
interfaceid=json.loads(response.text)["result"][0]["interfaces"][0]["interfaceid"]
host_id=json.loads(response.text)["result"][0]["hostid"]

response=zb.template.get(
        {
            "output":"extend",
            "filter": 
            {
                "host": ["Template_webpress_ngxacc_status"]
            }
        })
templateid=json.loads(response.text)["result"][0]["templateid"]
params={
        "output":"extend",
        "hostids":templateid
    }
response=zb.item.get(params)
item_list=json.loads(response.text)["result"]


for item in item_list:
    name_prefix=" ".join(item["name"].split()[1:])
    name="Total(webpress)-"+name_prefix
    key='grpsum["%s","%s",last,0]' %("Weibo_img-Webpress",item["key_"].strip())
    params={
        "name": name,
        "key_": key,
        "hostid": host_id,
        "type": 8,
        "value_type": 3,
        "interfaceid": interfaceid,
        "delay": 60,
        "application":["92472"]
    }
    response=zb.item.create(params)
    print json.dumps(json.loads(response.text),indent=2)
