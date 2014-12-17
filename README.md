pyzabbix
========

a tool based  on zabbix api  to operate zabbix more easily

zabbix api some likes restful api,it post a json to  api_jsonrpc.php
and the server will return data with json formate which contains the 
infomation you need or some error infomation;

make zabbix post-data-formate  simple, it like followings:

```
{
  "jsonrpc": "2.0",
  "method": "method.name", 
  "params": {
      "param_1_name": "param_1_value",
      "param_2_name": "param_2_value" 
  },
  "id": 1,
  "auth": "auth_string",
}
```

so at any time, I just need two arguement 
*   **method** its type is a string like "user.login","item.create",etc.
*   **params** its type is a dict

afer my encapsulation,you just need to pass one arguement that is params. 

and the api can be used to pass the method like:
```
zb.**host.get**(params_dict)
```
Thanks to [pyzabbix](https://github.com/lukecyca/pyzabbix),
It inspires me to use python magic method like ** __getattr__** to  make the code much cleaner

