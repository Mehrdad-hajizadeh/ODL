import pandas as pd
from collector import parser
from graph import Graph
import random
from gui import GUI
url = 'http://10.10.0.10:8181/restconf/operational/network-topology:network-topology' #main addresss
#url='http://10.10.0.10:8181/restconf/operational/network-topology:network-topology/topology/flow:1'
#url='http://10.10.0.10:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:3/node-connector/openflow:3:10'
#url= 'http://10.10.0.10:8181/restconf/operations/path-computation:get-constrained-path'
p=parser(url)
graph=Graph()

print(p.get_data_by_restapi())
#print(p.topology_node_port('openflow:1985587783700'))
#print(p.topology_node())
#print(p.topology_link())
print(p.topology_list())
print(p.topology_link())
'''
#pars json and return node list
edges=p.topology_link()


#create edges with random values between 1 and 10(as cost)
for item in range(len(edges)):
    edges[item].append((random.randint(1,10)))
for edge in edges:
    graph.add_edge(*edge)


#define GUI object based on edges
gui=GUI(edges)

#fucntion return g as info about nodes/edges in graph and position of each node for draw
g,pos=gui.create_topology_graph()

# show original topology with node and edge label
gui.show_graph(g,pos)


#take src and dst node from input
path_nodes=[]
path_nodes.extend([item for item in input("Enter the source and destination  nodes: ").split()])
src_node='openflow:'+path_nodes[0]
dst_node='openflow:'+path_nodes[1]
result=graph.dijsktra(src_node,dst_node)

gui.show_graph_shortest_path(g,result,pos)

'''
