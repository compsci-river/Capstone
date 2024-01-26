"""
Data Handling

River Sheppard
"""

import pandas as pd


def BatchUpdate(data,startTime,endTime, curDictionary):
    #Creates a subset of the dataframe that meets the time conditions
    df = data.loc[(data['TimeStamp']>=startTime)&(data['TimeStamp']<endTime)]
    #Loops through the subset
    for index, row in df.iterrows():
        #Updates the dictionary with key of mac address and value of timestamp
        curDictionary[row['MAC']] = row['TimeStamp']
    #Returns the updated dictionary
    return curDictionary

def TestBatchUpdate(data,startTime,endTime, curDictionary):
    #loops through the dataframe
    for index,row in data.iterrows():
        #Checks if the current row meets the time conditions
        if row['TimeStamp']>=startTime and row['TimeStamp']<endTime:
            #Updates the dictionary with key of mac address and value of timestamp
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
