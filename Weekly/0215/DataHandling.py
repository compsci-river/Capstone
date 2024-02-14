"""
Data Handling

River Sheppard
"""

import pandas as pd

#Updates the dictionary with a period of time
#data: DataFrame
#startTime: int
#endTime: int
#curDict: Dictionary
def BatchUpdate(data,startTime,endTime, curDict):
    #Creates a subset of the dataframe that meets the time conditions
    df = data.loc[(data['TimeStamp']>=startTime)&(data['TimeStamp']<endTime)]
    #Loops through the subset
    for index, row in df.iterrows():
        #Updates the dictionary with key of mac address and value of timestamp
        curDict[row['MAC']] = row['TimeStamp']
    #Returns the updated dictionary
    return curDict

def SiteAlignment(data,startTime,endTime,dicts):
    for i in range(len(data)):
        dicts[i] = BatchUpdate(data[i],startTime,endTime,dicts[i])
    return dicts

def ComputeTravelTimes(interval,maxTime,dictOne,dictTwo):
    temp = [[],[]]
    for key in dictOne:
        if key in dictTwo:
            if max(dictOne[key],dictTwo[key]) > maxTime-interval:
                #option here to add a max valid time
                dif = dictOne[key]-dictTwo[key]
                if dif > 0:
                    temp[0].append([dictOne[key],dif,key])
                else:
                    temp[1].append([dictTwo[key],abs(dif),key])
    return temp






if __name__ == "__main__":
    print('Main - DataHandling.py')

