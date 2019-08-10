# First of all lets look at some vocabulary terms.
# Degree: Degree describes a node's connectedness.
# Successors: A successory node is a node that could serve as a backup and potentially replace an influential node in a 
# network. The function of a succesor node is to preserve the flow of influence throughout a network in the case where 
# an important node is removed.
# Neighbours: Neighbours are adjacent nodes in a network.
# In-degree: The theory is that if a person or profile has a lot of inbound connections, then they are considered 
# prestigious, because many different people and porfiles want to connect with them.
# Out-degree: If a person or profile has a lot of outgoing connections, however, then they are sometime considered 
# inflential. That is because, in theory, these people have more of a platfrom accross which to engage and interact 
# with their many outbound connections.

#%%
import numpy as numpy
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb

import networkx as nx

from pylab import rcParams


#%%
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')

#%%
DG = nx.gn_graph(7,seed=25)

for line in nx.generate_edgelist(DG,data = False):
    print(line)

DG.node[0]['name'] = 'Alice'
DG.node[1]["name"] = 'Bob'
DG.node[2]["name"] = 'Claire'
DG.node[3]["name"] = 'Dennis'
DG.node[4]["name"] = 'Esther'
DG.node[5]["name"] = 'Frank'
DG.node[6]["name"] = 'George'

#%%
G = DG.to_undirected()


#%%
print(nx.info(DG))

#%%
# Considering degrees in a social  network
DG.degree()


#%%
# Identifying successor nodes
nx.draw_circular(DG, node_color ='bisque', with_labels = True)


#%%
list(DG.successors(3))


#%%
# All out-bound directions
list(DG.neighbors(4))

#%%
# Undirected neighbours
list(G.neighbors(4))

#%%
