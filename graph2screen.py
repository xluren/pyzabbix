from pyzabbix import zabbixapi
import json
url="url/zabbix/api_jsonrpc.php"
zb=zabbixapi(url=url,user="undefined",password="undefined")

def get_graph_id(hostid,graph_name):
    response=zb.graph.get(
            {
            "output": "extend",
            "sortfield": "name",
            "hostids": hostid})
    print json.dumps(json.loads(response.text),indent=2)
    for graph in json.loads(response.text)["result"]:
        print graph["name"] , graph_name
        if  graph["name"] == graph_name:
            print graph["graphid"]
            return graph["graphid"]


def get_hostid(host_name):
    response=zb.host.get(
            {
                "output":"extend",
                "filter":
                {
                    "host":host_name
                }
            })
    print json.dumps(json.loads(response.text),indent=2)
    return  json.loads(response.text)["result"][0]["hostid"]

def create_screen(x_length,graph_ids,screen_name):
    '''
    {
        "jsonrpc": "2.0",
        "method": "screen.create",
        "params": {
            "name": "Graphs",
            "hsize": 3,
            "vsize": 2,
            "screenitems": [
                {
                    "resourcetype": 0,
                    "resourceid": "612",
                    "rowspan": 0,
                    "colspan": 0,
                    "x": 0,
                    "y": 0
                }
            ]
        },
        "auth": "038e1d7b1735c6a5436ee9eae095879e",
        "id": 1
    }
    '''
    screenitems=[]
    ids_length=len(graph_ids)
    for y in xrange(ids_length/x_length):
        for x in xrange(x_length):
            print x,y
            item_dict={
                "resourcetype": 0,
                "resourceid": graph_ids[y*x_length+x],
                "x": y,
                "y": x
            }
            screenitems.append(item_dict)
    response=zb.screen.create({
        "name": screen_name,
        "hsize": ids_length/x_length+1,
        "vsize": x_length,
        "screenitems":screenitems
    })
    print json.dumps(json.loads(response.text),indent=2)
    


host_list=["backup"]
graph_ids={}
i=0
for host in host_list:
    hostid = get_hostid(host)
    graphid = get_graph_id(hostid,"CPU utilization")
    graph_ids[i]=graphid
    i+=1
print graph_ids
create_screen(x_length=2,graph_ids=graph_ids,screen_name="world")
