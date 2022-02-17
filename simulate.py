# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:29:48 2022

@author: n
"""
import networkx as nx
import random


"""
SCRIPT TO FIND THE NUMBER OF TIMES A BIT IS TRANSMITTED BEFORE NETWORK SEVERED
"""

discovered=[]


G=nx.fast_gnp_random_graph(20, .5, seed=None, directed=False) #Generate a random graph of size 20
if nx.is_connected(G)==False: #ensures resulting graph is connected
    while nx.is_connected(G)==False: 
        G=nx.fast_gnp_random_graph(20, .5, seed=None, directed=False) #generate random graphs with 10 nodes
node=G.nodes(1) #stars at node 1


traillength=0 #begins counting the trail length; imagine a single bit of data taking a random walk along the edges available to it at each vertex it visits
while nx.is_connected(G)==True: #stops when the network has been severed into two, losing cohesion
    traillength+=1 
    if random.uniform(0,1)<=.05: # probability of discovery at each bit transmission: 5%.
        discoverednode=min(list(G.nodes)) #pick a node to "discover"
        try:
            G.remove_nodes_from(G.neighbors(discoverednode)) #remove neighboring nodes (all neighboring nodes get "discovered" upon discovery of the original node)
            G.remove_node(discoverednode) #remove the originally discovered node too
        except: continue

    
    node= random.choice(list(G.neighbors(random.choice(list(G.nodes))))) #picks a new node to travel to
        
nx.draw(G)