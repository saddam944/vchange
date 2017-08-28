import glob, os
import sys
import re
import pandas as pd
import csv
from os.path import basename
from datetime import datetime,date, time, timedelta
import time

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
                    
