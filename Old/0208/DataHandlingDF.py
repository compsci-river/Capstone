"""
Data Handling - DataFrame Implementation

River Sheppard
"""

import pandas as pd

def BatchUpdate(data,startTime,endTime,curDF):
    df = data.loc[(data['TimeStamp']>=startTime)&(data['TimeStamp']<endTime)]
    for index, row in df.iterrows():
        curDF.loc[row['MAC'],'TimeStamp'] = row['TimeStamp']
    return curDF

def SiteAlignment(data,startTime,endTime,dfs):
    for i in range(len(data)):
        dfs[i] = BatchUpdate(data[i],startTime,endTime,dfs[i])
    return dfs

def CountOccurances(interval,maxTime,curDF):
    return len(curDF.loc[curDF['TimeStamp'] > maxTime-interval])
