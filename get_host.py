from pyzabbix import zabbixapi

url="http://10.210.71.145/zabbix/api_jsonrpc.php"
zb=zabbixapi(url=url,user="admin",password="zabbix")
response=zb.host.get({"output":["hostid","extend"],"filter": {"host":"test.144"}})
print response.text
