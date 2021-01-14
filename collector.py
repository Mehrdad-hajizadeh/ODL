import requests  # library should be installed
from requests.auth import HTTPBasicAuth
import json


class parser:
    def __init__(self,url='http://localhost:8181/restconf/operational/network-topology:network-topology'):
        self.url=url

    def get_data_by_restapi(self):
        headers = {"Accept": "application/json"}
        response = requests.get(self.url, headers=headers, auth=HTTPBasicAuth("admin", "admin"))
        ##json.load method converts JSON string to Python Object
        return json.loads(response.text)

    def put_data_by_restapi(url):
        pass

    def topology_list(self):  # return node with its ports in a list
        node_list = []
        parsed=self.get_data_by_restapi()
        for nodes in parsed["network-topology"]["topology"][2]["node"]:
            print(nodes["node-id"])
            #for sub in nodes:
                #print(nodes["node-id"])
                    #node = {}
                #node['id'] = sub['node-id']
                #for port in sub['termination-point']:
                    #node['tpid'] = port['tp-id']
                   # node_list.append(node.copy())
        #print(node_list)

    def topology_node(self):  # take parsed and return list of all nodes in parsed
        node_list = []
        parsed = self.get_data_by_restapi()
        for nodes in parsed["network-topology"]["topology"][2]["node"]:
                node = {}
                node = nodes['node-id']
                node_list.append(node)
        return node_list

    def topology_node_port(self, node):  # take parsed and input node to return list of all associated ports of the node
        node_port = []
        parsed = self.get_data_by_restapi()
        nodes = parsed["network-topology"]["topology"][2]["node"]
        for sub in nodes:
            if sub["node-id"] == node:
                for port in sub['termination-point']:
                    node_port.append(port['tp-id'])
        return (node_port)

    def topology_link(self):
        parsed = self.get_data_by_restapi()
        links = []  # a list containing links
        for link in parsed["network-topology"]["topology"][2]["link"]:
            links.append(list((((link["source"]["source-node"]), (link["destination"]["dest-node"])))))
        return links

    def topology_host(self):
        pass


