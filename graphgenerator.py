# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 11:08:17 2022

@author: n
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
values=np.zeros(500) #array containing mu values of each graph
prev=nx.fast_gnp_random_graph(10, .5, seed=None, directed=False) #generates a graph of given order (10)
average=0
if nx.is_connected(prev)==False: #ensures resulting graph is connected
    while nx.is_connected(prev)==False:
        prev=nx.fast_gnp_random_graph(10, .5, seed=None, directed=False)
for t in range(0,500):

    print(t)
    G=nx.fast_gnp_random_graph(10, .5, seed=None, directed=False) #generate random graphs with 10 nodes
    if nx.is_connected(G)==False: #ensure that the graphs are connected; if not, regenerate
        while nx.is_connected(G)==False:
            G=nx.fast_gnp_random_graph(10, .5, seed=None, directed=False)
            
    n= G.number_of_nodes()#n
    m= G.number_of_edges() #m
    n_prev=prev.number_of_nodes()
    m_prev=prev.number_of_edges()
    sum_of_degrees_squared=0
    sum_of_degrees_squared_prev=0
    total_dist=0
    
    #####CALCULATIONS FOR THE NEW GRAPH GENERATION
    path=list(nx.all_pairs_shortest_path(G))  #geodescic distances between all node pairs
    for j in range(0,len(list(G.nodes()))):
        sum_of_degrees_squared+=G.degree[j]**2 #quantity is used in mu value from secanario 3 in paper
    path=nx.all_pairs_shortest_path(G)
    x=(list(path))
    sum1=0
    for i in range(0,len(x)): #Calculating total distance T as referenced in paper
        for j in range(0,len(x[i][1])):
            
            vals=list(x[i][1].values())
            for p in range(0,len(vals)):
                sum1+=len(vals[p])
    total_dist=sum1 #calling total_dist the T value
                
    #CALCULATIONS FOR THE EXISTING GRAPH GENERATION
    path=list(nx.all_pairs_shortest_path(prev))
    for j in range(0,len(list(prev.nodes()))):
        sum_of_degrees_squared_prev+=prev.degree[j]**2 #quantity is used in mu value from scenario 3 in paper
    path=nx.all_pairs_shortest_path(prev)
    x=(list(path))
    sum1=0
    for i in range(0,len(x)): #calculating the total_dist T value
        for j in range(0,len(x[i][1])):
            
            vals=list(x[i][1].values())
            for p in range(0,len(vals)):
                sum1+=len(vals[p]) 
    total_dist_prev=sum1
    values[t]=((n-1) / (2*m+n)) * (2*m*(n-2)+n*(n-1)-sum_of_degrees_squared)/total_dist
    if ((n-1) / (2*m+n)) * (2*m*(n-2)+n*(n-1)-sum_of_degrees_squared)/total_dist > ((n_prev-1) / (2*m_prev+n_prev)) * (2*m_prev*(n_prev-2)+n_prev*(n_prev-1)-sum_of_degrees_squared_prev)/total_dist_prev:
        prev=G #if new mu value is bigger than old new value, save this new graph


prev =nx.draw(prev) #draw the graph with the highest mu value
plt.show() #show the graph with highest mu value
print(((n_prev-1) / (2*m_prev+n_prev)) * (2*m_prev*(n_prev-2)+n_prev*(n_prev-1)-sum_of_degrees_squared_prev)/total_dist_prev)
#print highest mu value; way lower than those found in paper, even for fenerations of up to 50,000 graphs
#generating up to 500,000 graphs is going to take hours...