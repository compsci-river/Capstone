"""
Data Handling

River Sheppard
"""

import pandas as pd

def BatchUpdate(data,startTime,endTime, curDictionary):
    df = data.loc[(data['TimeStamp']>=startTime)&(data['TimeStamp']<endTime)]
    for index, row in df.iterrows():
        curDictionary[row['MAC']] = row['TimeStamp']
    return curDictionary

def TestBatchUpdate(data,startTime,endTime, curDictionary):
    for index,row in data.iterrows():
        if row['TimeStamp'] >= startTime and row['TimeStamp'] < endTime:
            curDictionary[row['MAC']] = row['TimeStamp']
    return curDictionary

def SiteAlignment(data,startTime,endTime,dicts):
    for i in range(len(data)):
        dicts[i] = TestBatchUpdate(data[i],startTime,endTime,dicts[i])
    return dicts

#Two sites
def ComputeTravelTimes(dOne,dTwo):
    temp = []
    for key in dOne:
        if key in dTwo:
            temp.append([dOne[key],abs(dOne[key]-dTwo[key])])
    print("ComputeTravelTimes currently has the absolute value of travel time from when I was testing")
    return pd.DataFrame(temp)
