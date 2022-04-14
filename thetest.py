# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:25:12 2022

@author: n
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
# G=nx.DiGraph()
# G.add_node(1,pos=(-1,0))
# G.add_node(2,pos=(0,1))
# G.add_node(3,pos=(1,0))
# G.add_node(4,pos=(0,-1))
# G.add_node(5,pos=(0,0))
# G.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,1),(2,5),(3,5)])

# G[1][2]['weight'] = random.randint(1,10)
# G[2][3]['weight'] = random.randint(1,10)
# G[3][4]['weight'] = random.randint(1,10)
# G[4][5]['weight'] = random.randint(1,10)
# G[5][1]['weight'] = random.randint(1,10)
# G[2][5]['weight'] = random.randint(1,10)
# G[3][5]['weight'] = random.randint(1,10)
labels = nx.get_edge_attributes(G,'weight')
inflows=[]
outflows=[]
for i in list(G.nodes()):
    inflow=0
    inedges=list(G.in_edges(i))
    for j in inedges:
        inflow+=labels.get(j)
    inflows.append(inflow)
    
    
    outflow=0
    outedges=list(G.out_edges(i))
    for j in outedges:
        outflow+=labels.get(j)
    outflows.append(outflow)
    
probs=[]
for i in range(0,len(inflows)):
    probs.append((inflows[i]+outflows[i])/(np.sum(inflows)+np.sum(outflows)))
halfnormalized=[]
for i in range(0,len(probs)):
    halfnormalized.append((probs[i]-np.mean(probs))/np.std(probs))
    #G[i]['weight']=

netflows=[]
for i in range(0,len(inflows)):
    netflows.append(inflows[i]-outflows[i])

yvals=[]
for i in range(0,len(inflows)):
    numerator=2*(outflows[i]/inflows[i])-2*min(netflows)
    denominator=max(netflows)**2-min(netflows)**2+2*min(netflows)*(min(netflows)-max(netflows))
    yvals.append(numerator/denominator)
    
otherhalfnormalized=[]
for i in range(0,len(yvals)):
    otherhalfnormalized.append((yvals[i]-np.mean(yvals))/np.std(yvals))

totalnormalized=[]
for i in range(0,len(halfnormalized)):
    totalnormalized.append(halfnormalized[i]+otherhalfnormalized[i])
    

for i in range(0,len(totalnormalized)):
    if np.abs(totalnormalized[i])<1:
        while np.abs(totalnormalized[i])<1:
            for j in range(0,len(totalnormalized)):
                totalnormalized[j]=1.01*totalnormalized[j]  
            print(totalnormalized)
etothe=[]
for i in range(0,len(totalnormalized)):
    etothe.append(1.3**totalnormalized[i])
   
 

finalweights=[]
for i in range(0,len(etothe)):
    finalweights.append(3000*etothe[i]/np.sum(etothe))
for i in range(0,len(outflows)):
    print(outflows[i]/inflows[i])

pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos, with_labels=True,node_size=finalweights)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

