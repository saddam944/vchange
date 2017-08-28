
# coding: utf-8

# In[10]:

import numpy as np
import pandas as pd
import time
import datetime
import math
import csv
import re
import collections
path="E:/5_Vaib1985_.csv"
src=int(path[3:4])
df = pd.read_csv(path)
mentions=[]
ego="sham829"
count_mentions=0
nodes=[]
weight=[]
source=[]
ids=[] 
for index, row in df.iterrows():
    try:
        pat=re.findall("^(?!RT\s)(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9_]+)",row['tweet'])
        usr=pat[0]
        #usr=pat[0].strip()[4:-1]
        mentions.append(usr)
        #Retweeted.append(usr)
    except:
        continue      
        
userfrequency = {i:mentions.count(i) for i in mentions}
userfrequency        
srl=0
for key,val in userfrequency.items():
    print key,":",val
    nodes.append(key)
    weight.append(val)
    source.append(src)
    ids.append(srl)
    srl=srl+1
    
nodecsv=[]
edgecsv=[]
for t in range(len(nodes)):
    nodecsv.append([ids[t],nodes[t]])
    edgecsv.append([source[t],ids[t],"Directed",weight[t]])    
    
csvdataframe=pd.DataFrame(nodecsv,columns=['id', 'label'])
csvdataframe.to_csv("E:/mentions_nodes.csv",index=False)

csvdataframe=pd.DataFrame(edgecsv,columns=['Source', 'Target','Type','Weight'])
csvdataframe.to_csv("E:/mentions_edge.csv",index=False)


# In[ ]:



