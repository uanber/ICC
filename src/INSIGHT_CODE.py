
import pandas as pd
import sys
import argparse
import sys, pprint

sys.path.append('/Users/uma2103/anaconda/lib/python2.7/site-packages')

import networkx as nx


def fraud_detect(stream,length,phrase):  
    for i in range(len(stream)):
        if True in [stream[i][0] in L[k] and stream[i][1] in L[k] for k in range(len(L))]:
            if len(nx.shortest_path(G,stream[i][0],stream[i][1]))<=length+1:
                out.write('trusted')
                out.write('\n')
            else:
                out.write(phrase)
                out.write('\n')
        else:
            out.write(phrase)
            out.write('\n')    
    out.close()
    return out
    
    
parser = argparse.ArgumentParser(description='fraud detect')

#input files     
parser.add_argument('-f1', help='optional', required=True)
parser.add_argument('-f2', help='optional', required=True)

#output files
parser.add_argument('-o1', help='optional', required=True)
parser.add_argument('-o2', help='optional', required=True)
parser.add_argument('-o3', help='optional', required=True)    

args = parser.parse_args()  


#PATH='/Users/uma2103/Insight/'
#PATH='/Users/uma2103/Downloads/ICC-master/insight_testsuite/tests/test-1-paymo-trans/'

df=pd.read_csv(args.f1, header=None, skiprows=[0], sep=r",") 

# create a tuple 
F=[(df[1][i],df[2][i]) for i in range(len(df))] 

G = nx.Graph()
G.add_edges_from(F)
L=nx.connected_components(G);


# now read the stream data
#F_STREAM=random.sample(F,  30) #30 random sample from F

df_stream=pd.read_csv(args.f2, header=None, skiprows=[0], sep=r",")

F_STREAM = [(df_stream[1][i],df_stream[2][i]) for i in range(len(df_stream))] 




#PATH='/Users/uma2103/Insight/paymo_output/'
#files=['output1.txt','output2.txt','output3.txt']

files= [args.o1,args.o2,args.o3]
 
LINE1='unverified: not friend'
LINE2='unverified: not friend or 2nd degree friend'
LINE3='unverified: not friend or within 4th degree friends'
LINES=[LINE1, LINE2, LINE3]

for feature in [0,1,2]:
    
    out = open(files[feature],'w')
    
    if feature ==0:
        length = 1
    if feature ==1:
        length = 2
    if feature ==2:
        length = 4
    
    fraud_detect(F_STREAM,length,LINES[feature])  

  
