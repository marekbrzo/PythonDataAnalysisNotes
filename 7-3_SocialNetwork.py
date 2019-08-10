# Simulating a Social Network
# Three easy steps: 1. Generate graph object and edge list. 2. Assign attributes to graph nodes. 3. Visualize the network


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
# Generating a graph object and edgelist
DG = nx.gn_graph(7,seed=25)

for line in nx.generate_edgelist(DG,data = False):
    print(line)


#%%
# Assign attributes to nodes, such as name, weight, directions.
print(DG.node[0])


#%%
DG.node[0]["name"] = 'Alice'
print(DG.node[0])


#%%
DG.node[1]["name"] = 'Bob'
DG.node[2]["name"] = 'Claire'
DG.node[3]["name"] = 'Dennis'
DG.node[4]["name"] = 'Esther'
DG.node[5]["name"] = 'Frank'
DG.node[6]["name"] = 'George'



#%%
# Other methods to add to the nodes
DG.add_nodes_from([(0,{'age':25}),(1,{'age':31}),(2,{'age':18}),(3,{'age':47}),(4,{'age':22}),(5,{'age':23}),(6,{'age':50})])

print(DG.node[0])
#%%
DG.node[0]["gender"] = 'f'
DG.node[1]["gender"] = 'm'
DG.node[2]["gender"] = 'f'
DG.node[3]["gender"] = 'm'
DG.node[4]["gender"] = 'f'
DG.node[5]["gender"] = 'm'
DG.node[6]["gender"] = 'm'

print(DG.node[0])

#%%
nx.draw_circular(DG, node_color = 'bisque', with_labels = True)


#%%
# Labelling the graph
labeldict = {0:'Alice',1:'Bob',2:'Claire',3:'Dennis',4:'Esther',5:'Frank',6:'George'}
nx.draw_circular(DG, node_color = 'bisque', with_labels = True, labels =labeldict)

#%%
G = DG.to_undirected()
nx.draw_spectral(G, node_color = 'bisque', with_labels = True, labels =labeldict)

#%%
# Directional network graphs can tell us who is the most important person in the graph. Once we remove direction then the person become
# the least important