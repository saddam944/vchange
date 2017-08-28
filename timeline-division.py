import numpy as np
import pandas as pd
import time
import datetime
import math
import csv
import decimal


dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
df = pd.read_csv("E:/PS4AusGamer_.csv", parse_dates=['date'], date_parser=dateparse)

def intervalss():
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
    csvdataframe.to_csv("E:/PS4AusGamer_intervals.csv",index=False)
 
    
if __name__ == "__main__":
    segment_tweets()

