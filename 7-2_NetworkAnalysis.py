# NETWROK ANALYSIS
# Making graphs and visualizations for network analysis.
# Used in such cases as: Social Media Marketing Strategy, Infrastucture system design, finanical risk management, Public Health Management
# Network dynamics is becoming larger with social media.
# Network is a body of connected data that is evaluated during graph analysis.
# Graph is a data visualization schematic depicting the data that comprises a network.
# Network Analysis Vocabulary
# Nodes - the vertices around which a graph is formed.
# Edges - the lines that connect vertices within a graph structure.
# Directed graph (aka digraph) - a graph where there is a direction assigned to each edge that connects a node
# Directed edge - an edge feature that has been assigned a direction between nodes.
# Undirected graph - a graph where all edges are bidirectional
# Undirected edge - a bidirectional edge feature
# Graph size - the number of edges in a graph
# Graph order - the number of vertices in a graph
# Degree - the number of edges connected to a vertex, with loops counted twice.  A measure of connectiveness.
# Types of Graph Generators
# Graph drawing algorithms
# Network analysis algorithm
# Algorithmic routing for graphs
# Graph search algorithms
# Subgraph algorithms
# !pip install networkx

#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb 
import networkx as nx 

from pylab import rcParams

#%%
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')

#%%


#%%
G = nx.Graph()
nx.draw(G)

#%%
G.add_node(1)
nx.draw(G)

#%%
G.add_nodes_from([2,3,4,5,6,8,9,12,15,16])
nx.draw(G)

#%%
G.add_edges_from([(2,4),(2,6),(2,8),(2,12),(2,16),(3,6),(3,9),(3,12),(3,15),(4,8),(4,12),(4,16),(6,12),(8,16)])
nx.draw(G)


#%%
# Basic about drawing graph
# Shape of network
nx.draw_circular(G)


#%%
nx.draw_spring(G)


#%%
# Labels and coloring the plots
nx.draw_circular(G, node_color = 'bisque', with_labels = True)



#%%
# Removing nodes
G.remove_node(1)
nx.draw_circular(G, node_color = 'bisque', with_labels = True)


#%%
# Graph properties
# Show the stats.
sum_stats = nx.info(G)
print(sum_stats)


#%%
# CLoser views
print(nx.degree(G))


#%%
# An automatic graph generator, NO manual inputs needed.
G = nx.complete_graph(25)
nx.draw(G,node_color = 'bisque', with_labels = True)


#%%
G =nx.gnc_graph(7,seed = 25)
nx.draw(G, node_color = 'bisque', with_labels = True)

#%%
# Ego graph, Social networks use these.
ego_G = nx.ego_graph(G,3,radius=5)
nx.draw(G, node_color = 'bisque', with_labels = True)



#%%
