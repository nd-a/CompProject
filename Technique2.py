# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 10:05:48 2022

@author: n
"""

import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt



#BUILD SEED GRAPH HERE; CALL IT 'prev'; looks likea big circle; good enough I guess, couldn't get anything else to work
prev=nx.cycle_graph(8) #replace the number in parentheses with order of graph



values=np.zeros(500) #array containing mu values of each graph
#change the 500 values above and below to number of iterations (500,000 is going to take a while)
for t in range(0,500):
    print(t)
    try:
        
        node1=random.choice(list(prev.nodes())) #https://stackoverflow.com/questions/26768065/how-to-extract-random-nodes-from-networkx-graph
        node2=random.choice(list(prev.nodes())) #pick two random nodes
        if node1==node2:
            while node1==node2:
                node2=random.choice(list(prev.nodes())) #making sure two nodes aren't the same
        
        G=prev.copy()
        
        G.add_edge(node1,node2) #adds random edge to existing highest-mu graph
        
    
        
    except: continue
            
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
        # print(((n-1) / (2*m+n)) * (2*m*(n-2)+n*(n-1)-sum_of_degrees_squared)/total_dist)
        # print(((n_prev-1) / (2*m_prev+n_prev)) * (2*m_prev*(n_prev-2)+n_prev*(n_prev-1)-sum_of_degrees_squared_prev)/total_dist_prev)
        prev=G #if new mu value is bigger than old new value, save this new graph
        

#print(((n_prev-1) / (2*m_prev+n_prev)) * (2*m_prev*(n_prev-2)+n_prev*(n_prev-1)-sum_of_degrees_squared_prev)/total_dist_prev)
nx.draw(G)
plt.show()
plt.savefig("/Users/n/Downloads/figure1.png") #change to valid filepath
#print highest mu value; way lower than those found in paper, even for fenerations of up to 50,000 graphs
#generating up to 500,000 graphs is going to take hours...
