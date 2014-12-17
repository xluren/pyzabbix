from pyzabbix import zabbixapi
import json
url="http://10.210.71.145/zabbix/api_jsonrpc.php"

#login
zb=zabbixapi(url=url,user="admin",password="zabbix")
#graph.create
#refer:https://www.zabbix.com/documentation/2.4/manual/api/reference/graph/create

gitems=[]
gitems.append({"itemid":1100,"color":"","sortorder":"0"})
name="webpress ngxacc - /%s/ response time" % k
response=zb.graph.create(
        {
            "name": name, 
            "width": 900,
            "height": 200,
            "gitems":gitems
        })
print json.dumps(json.loads(response.text),indent=2)'''
