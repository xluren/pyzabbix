from pyzabbix import zabbixapi
import json
url="http://10.210.71.145/zabbix/api_jsonrpc.php"

#login
zb=zabbixapi(url=url,user="admin",password="zabbix")
#host.get
#api refer:https://www.zabbix.com/documentation/2.4/manual/api/reference/host/get
#notice:"templated_hosts":1 it means 
#templated_hosts    flag    Return both hosts and templates.
response=zb.host.get(
        {
            "output":["hostid","templated_hosts"],
            "templated_hosts":1,
            "filter": 
            {
                "name":"Template_webpress_ngxacc_status"
            }
        })
print "with (templated_hosts:1)"
print json.dumps(json.loads(response.text),indent=2)
hostid=json.loads(response.text)["result"][0]["hostid"]
print "without (templated_hosts:1)"
response=zb.host.get(
        {
            "output":["hostid","templated_hosts"],
            "filter": 
            {
                "name":"Template_webpress_ngxacc_status"
            }
        })
print json.dumps(json.loads(response.text),indent=2)

#item.create add item to a templates 
#api refer: https://www.zabbix.com/documentation/2.4/manual/api/reference/item/create
#attention:
#interfaceid (required)  string  ID of the item's host interface. Used only for host items. 
#**but** Optional for Zabbix agent (active), Zabbix internal, Zabbix trapper, Zabbix aggregate, database monitor and calculated items.

name="webpress ngxacc pictype==webp180 and response time (100-200ms]"
key="webpress_ngxacc_webp180_100-200ms"
params={
    "name": name,
    "key_": "webpress_ngxacc_"+pic_type+"_"+time_item,
    "hostid": hostid,
    "type": 2,
    "value_type": 3,
    "interfaceid": "",
    "delay": 60
}
response=zb.item.create(params)
print json.dumps(json.loads(response.text),indent=2)
