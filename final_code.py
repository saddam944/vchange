import logging
import tweepy
import numpy as np
import pandas as pd
import time
import datetime
import math
import csv
import decimal
import os
import re
import collections
from os.path import basename
from datetime import datetime,date, time, timedelta
import time
    
access_key = "your access key"
access_secret = "your access secret"
consumer_key = "your consumer key"
consumer_secret = "your consumer secret"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
uname=''

#dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
#df = pd.read_csv("E:/"+uname+"_.csv", parse_dates=['date'], date_parser=dateparse)

def get_followingss(user_name):
    for user in tweepy.Cursor(api.friends, screen_name=user_name).items():
        print user.screen_name
        
def get_followerss(user_name):
    for user in tweepy.Cursor(api.followers, screen_name=user_name).items():
        print user.screen_name
        
        
def get_mentionss(user_name):       
    mentions = api.mentions_timeline(count=1)
    for mention in mentions:
        print mention.text
        print mention.user_name.screen_name
        
        
def intervalss():
    dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    df = pd.read_csv("E:/"+uname+"_.csv", parse_dates=['date'], date_parser=dateparse)
    flag=0
    dates=[]
    for index, row in df.iterrows():
        if flag==0:
            end=row['date']
            flag=1    
        if index==len(df)-1:
            start=row['date']
    
    gap=end-start
    dys=float(gap.days)
    slots=decimal.Decimal(dys/90)
    intervals=math.ceil(slots)
    
    three_months = datetime.timedelta(3*365/12)
    dates.append(start)
    for i in range(int(intervals)):
        dates.append(start+three_months)
        start=start+three_months
    return dates
    
def segment_tweets():
    dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    df = pd.read_csv("E:/"+uname+"_.csv", parse_dates=['date'], date_parser=dateparse)
    interval_dates=intervalss()
    interval_length=len(interval_dates)
    i=0
    segmented_tweets=[]
    while i<(interval_length-1):
        for index, row in df.iterrows():
            if row['date']>=interval_dates[i] and row['date']<interval_dates[i+1]:
                #print row['tweet']
                segmented_tweets.append([row['date'],row['tweet']])
        segmented_tweets.append(["This is a delimenter"])
        i=i+1    
    csvdataframe=pd.DataFrame(segmented_tweets,columns=['date', 'tweets'])
    csvdataframe.to_csv("E:/"+uname+"_intervals.csv",index=False)

    
def chunking_timeslot_files():
    slots=[]
    pair_slots=[]
    final_slots=[]
    tempList=[]
    slots.append(2)
    df = pd.read_csv("E:/"+uname+"_intervals.csv")
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
    if not os.path.isdir("E:/"+uname):
        os.makedirs("E:/"+uname)
    for tm in range(len(final_slots)):
        csvdataframe=pd.DataFrame(final_slots[tm],columns=['date', 'tweets'])
        csvdataframe.to_csv("E:/"+uname+"/"+uname+"_int"+str(tm)+".csv",index=False)
        
def retweet_network(uname):
    Retweeted=[]
    nodes=[]
    weight=[]
    ids=[] 
    source=[]
    df = pd.read_csv("E:/"+uname+"_.csv")
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
    csvdataframe.to_csv("E:/retweet_nodes.csv",index=False)

    csvdataframe=pd.DataFrame(edgecsv,columns=['Source', 'Target','Type','Weight'])
    csvdataframe.to_csv("E:/retweet_edge.csv",index=False)
    
def mentionss():
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
    
def find_alters_within_egotime():
    egodates=[]
    alterdates=[]
    egopath="E:/EGO_rokshana_alam.csv"
    with open(egopath,'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            rows = list(reader)
            for row in rows:
                if row['date']:
                    if row['ego']=="yes":
                    #print row['date']
                        egodates.append(row['date'])
                    
    one_month = timedelta(365/12)
    with open(egopath,'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            rows = list(reader)
            for e in egodates:
                #print e
                ego_tm=datetime.strptime(e, '%m/%d/%Y %H:%M')
                for row in rows:
                    if row['date']:
                        if row['alter']=="yes":
                            #print row['date']
                            #egodates.append(row['date'])
                            alter_tm=datetime.strptime(row['date'], '%m/%d/%Y %H:%M')
                            alter_range_tm=alter_tm+one_month
                            #print alter_tm,alter_range_tm
                            if (ego_tm>alter_tm) & (ego_tm<alter_range_tm):
                                print ego_tm,row['name']+"-"+row['time-interval'],alter_tm
    
if __name__ == '__main__':
    #uname = raw_input('Enter your user-name: ')
    #get_followingss(uname)
    #get_followerss(uname)
    #get_mentionss(uname)
    #segment_tweets()
    #chunking_timeslot_files()
    #retweet_network(uname)
    #mentionss()
    find_alters_within_egotime()

