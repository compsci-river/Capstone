"""
Test

River Sheppard
"""
import pandas as pd
import ProcessBluetoothData as BTDF
import DataHandling as dh
import time

def TestBatchUpdate(data,minTime,interval,n):
    print('BatchUpdate()')
    cDict = {}
    temp = minTime
    mCount = 0
    start = time.time()
    while temp < minTime+n*interval:
        cDict = dh.BatchUpdate(data,temp,temp+interval,cDict)
        temp += interval
        mCount += 1
    end = time.time()
    mTime = end - start
    print(str(len(cDict))+' entries\n'+str(mCount)+' iterations in '+str(mTime)+' seconds',end='\n\n')

    print('TestBatchUpdate()')
    tDict = {}
    temp = minTime
    start = time.time()
    tCount = 0
    while temp < minTime+n*interval:
        tDict = dh.TestBatchUpdate(data,temp,temp+interval,tDict)
        temp += interval
        tCount += 1
    end = time.time()
    tTime = end - start
    print(str(len(tDict))+' entries\n'+str(tCount)+' iterations in '+str(tTime)+' seconds',end='\n\n')

    print('Checking equivalence:')
    if mCount == tCount:
        print('Equal number of entries')
        equal = 0
        k = list(cDict.keys())
        for i in range(len(k)):
            if k[i] == k[i]:
                if cDict[k[i]] == tDict[k[i]]:
                    equal += 1
        print(str(100*equal/len(cDict))+'% of entries equal')
        if equal == len(cDict):
            print('Results are equivilent')
    

def main():
    
    strDataFolder = './data/'
    strFileName = ['FAWNDALE_trafficnow-data (05-11-23).gz',
                   'PINE_GROVE_trafficnow-data (05-11-23).gz']
    
    interval = 600
    n = 10
    data = BTDF.BTgzToDF(strDataFolder+strFileName[0])
    minTime = data['TimeStamp'].min()
    maxTime = data['TimeStamp'].max()

    print('Loading first ten intervals of 600 seconds from Fawndale dataset.',end='\n\n')
    TestBatchUpdate(data,minTime,interval,n)

    

    

    
    """
    data = []
    dictionaries = []
    for i in range(len(strFileName)):
        strPath = strDataFolder + strFileName[i]
        data.append(BTDF.BTgzToDF(strPath))
        dictionaries.append({})

    
    minTime = min(data[0]['TimeStamp'].min(),data[1]['TimeStamp'].min())
    maxTime = max(data[0]['TimeStamp'].max(),data[1]['TimeStamp'].max())
        
    while minTime < maxTime:
        curDictionary = dh.SiteAlignment(data,minTime,minTime+interval,dictionaries)
        minTime += interval
        
    #for i in range(len(dictionaries)):
        #print(len(dictionaries[i]))

    df = dh.ComputeTravelTimes(dictionaries[0],dictionaries[1])
    #print(df)

    s = df[1]
    print(s.describe())
    """
    

if __name__ == "__main__":
    main()
    print("Testing - Main.")
