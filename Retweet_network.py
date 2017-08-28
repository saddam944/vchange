import numpy as np
import pandas as pd
import time
import datetime
import math
import csv
import re
import collections

Retweeted=[]
nodes=[]
weight=[]
ids=[]
df = pd.read_csv("E:/EthanThoren_.csv")
for index, row in df.iterrows():
    try:
        pat=re.findall('^RT\s@.*?:\s',row['tweet'])
        #print pat
        usr=pat[0].strip()[4:-1]
        Retweeted.append(usr)
    except:
        continue

userfrequency = {i:Retweeted.count(i) for i in Retweeted}
#print type(userlist)
srl=0
for key,val in userfrequency.items():
    #print key,":",val
    nodes.append(key)
    weight.append(val)
    source.append(1)
    ids.append(srl)
    srl=srl+1
    

nodecsv=[]
edgecsv=[]
for t in range(len(nodes)):
    nodecsv.append([ids[t],nodes[t]])
    edgecsv.append([source[t],ids[t],"Directed",weight[t]])
    
    
csvdataframe=pd.DataFrame(nodecsv,columns=['id', 'label'])
csvdataframe.to_csv("E:/nodes.csv",index=False)

csvdataframe=pd.DataFrame(edgecsv,columns=['Source', 'Target','Type','Weight'])
csvdataframe.to_csv("E:/edge.csv",index=False)

