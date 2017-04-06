#!/usr/bin/env python

import networkx as nx
import pandas as pd


# read the base data to create the netwrk 
file_batch='/Users/uma2103/Insight/paymo_input/batch_payment.txt'
df=pd.read_csv(file_batch, header=None, skiprows=[0], sep=r",") 

# create a tuple for ID1 and ID2 
F=[(df[1][i],df[2][i]) for i in range(len(df))] 

# create the network graph
G = nx.Graph()
G.add_edges_from(F)

# check connectivity of the graph:
# nx.connected_components returns a list of lists of all the connected parts in base graph 
L=nx.connected_components(G)


# now read the stream data
file_stream='/Users/uma2103/Insight/paymo_input/stream_payment.txt'
df_stream=pd.read_csv(file_stream, header=None, skiprows=[0], sep=r",")

# form a tuple of streamed data (do we really need this)? better to have tuples 
F_STREAM = [(df_stream[1][i],df_stream[2][i]) for i in range(len(df_stream))] 



PATH='/Users/uma2103/Insight/paymo_output/'
files=['output1.txt','output2.txt','output3.txt']


for feature in [0,1,2]:
    
    out = open(PATH+files[feature],'w')
    
    if feature ==0:
        length = 1
    if feature ==1:
        length = 2
    if feature ==2:
        length = 4
    
    fraud_detect(F_STREAM,length)



# a funtion for fraud detection that returns an output txt file
# and takes two arguments: stream, which is the tuple of the stream
# data, and length, an integer that specify the neighbor strength,
# in other words the feature
    
def fraud_detect(stream,length):
    
    for i in range(len(stream)):
        if True in [stream[i][0] in L[k] and stream[i][1] in L[k] for k in range(len(L))]:
            if len(nx.shortest_path(G,stream[i][0],stream[i][1]))<=length+1:
                out.write('trusted')
                out.write('\n')
            else:
                out.write('unverified')
                out.write('\n')
        else:
            out.write('unverified')
            out.write('\n')
           
    out.close()
    return out



