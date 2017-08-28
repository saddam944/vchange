
# coding: utf-8

# In[29]:

import csv
import pandas as pd

slots=[]
pair_slots=[]
final_slots=[]
tempList=[]
slots.append(2)
df = pd.read_csv("E:/PS4AusGamer_intervals.csv")
for index, row in df.iterrows():
    if row['date']=="This is a delimenter":
            slots.append(index+2)        
        
for p1, p2 in zip(slots, slots[1:]):
    pair_slots.append([p1,p2])
    
for idx in range(len(pair_slots)):
    for index, row in df.iterrows():
        if index>int(pair_slots[idx][0]) and index<int(pair_slots[idx][1]):
            tempList.append([row['date'],row['tweets']])
            #print row['tweets']
    #print pair_slots[idx][0],pair_slots[idx][1]
    #print "*************************************************************************"
    final_slots.append(tempList[:])
    del tempList[:]

    #print len(final_slots)

for tm in range(len(final_slots)):
    csvdataframe=pd.DataFrame(final_slots[tm],columns=['date', 'tweets'])
    csvdataframe.to_csv("E:/PS4AusGamer_int"+str(tm)+".csv",index=False)


# In[ ]:



