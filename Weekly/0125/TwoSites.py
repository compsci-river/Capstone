"""
Two Sites

River Sheppard
"""

import pandas as pd
import BTgzToDF as BTgz
import DfToSeqDict as DfToDict

def SiteAlignment(data,startTime,endTime,dictionaries):
    for i in range(len(data)):
        dictionaries[i] = DfToDict.BatchUpdate(data[i],startTime,endTime,dictionaries[i])
    return dictionaries

"""
Test
"""

def main():
    strDataFolder = './data/'
    strFileName = ['FAWNDALE_trafficnow-data (05-11-23).gz',
                   'PINE_GROVE_trafficnow-data (05-11-23).gz']
    interval = 600

    data = []
    dictionaries = []
    for i in range(len(strFileName)):
        strPath = strDataFolder + strFileName[i]
        data.append(BTgz.BTgzToDF(strPath))
        dictionaries.append({})

    
    minTime = min(data[0]['TimeStamp'].min(),data[1]['TimeStamp'].min())
    maxTime = max(data[0]['TimeStamp'].max(),data[1]['TimeStamp'].max())
        
    while minTime < maxTime:
        curDictionary = SiteAlignment(data,minTime,minTime+interval,dictionaries)
        minTime += interval
        
    for i in range(len(dictionaries)):
        print(len(dictionaries[i]))
    

if __name__ == "__main__":
    main()
    print("Two Sites - Main.")
    
