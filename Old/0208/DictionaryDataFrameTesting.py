"""
River Sheppard

Dictionary vs DataFrame Implementation
"""

import time
import pandas as pd

import ProcessBluetoothData as BTDF
import DataHandling_RS as DictDH
import DataHandlingDF as DFDH

def testDictionary(data,minTime,maxTime,interval,n):
    dicts = []
    counts = []
    for i in range(len(data)):
        dicts.append({})
        counts.append([])
    count = 1
    while minTime < maxTime:
        dicts = DictDH.SiteAlignment(data,minTime,minTime+interval,dicts)
        minTime += interval
        if count%n == 0:
            for i in range(len(counts)):
                counts[i].append(DictDH.CountOccurances(interval*n,minTime,dicts[i]))
        count += 1
    for i in range(len(counts)):
        print(counts[i])

def testDataFrame(data,minTime,maxTime,interval,n):
    dfs = []
    counts = []
    for i in range(len(data)):
        dfs.append(pd.DataFrame(columns=['MAC','TimeStamp']).set_index('MAC'))
        counts.append([])
    count = 1
    while minTime < maxTime:
        dfs = DFDH.SiteAlignment(data,minTime,minTime+interval,dfs)
        minTime += interval
        if count%n == 0:
            for i in range(len(counts)):
                counts[i].append(DFDH.CountOccurances(interval*n,minTime,dfs[i]))
        count += 1
    for i in range(len(counts)):
        print(counts[i])

def testTravelTimes(data,minTime,maxTime,interval,n):
    dicts = []
    counts = [[],[]]
    times = [[],[]]
    for i in range(len(data)):
        dicts.append({})
    count = 1
    while minTime < maxTime:
        dicts = DictDH.SiteAlignment(data,minTime,minTime+interval,dicts)
        minTime += interval
        if count%n == 0:
            temp = DictDH.ComputeTravelTimes(interval*n,minTime,dicts[0],dicts[1])
            times[0] += temp[0]
            times[1] += temp[1]
        count += 1
    pd.DataFrame(times[0],columns=['TimeStamp','TravelTime','MAC']).to_csv('./North.csv',index=False)
    pd.DataFrame(times[1],columns=['TimeStamp','TravelTime','MAC']).to_csv('./South.csv',index=False)

def testCountTravels(data,minTime,maxTime,interval,n):
    dicts = []
    counts = []
    for i in range(len(data)):
        dicts.append({})
    count = 1
    while minTime < maxTime:
        dicts = DictDH.SiteAlignment(data,minTime,minTime+interval,dicts)
        minTime += interval
        if count%n == 0:
            temp = DictDH.ComputeTravelTimes(interval*n,minTime,dicts[0],dicts[1])
            counts.append([minTime,len(temp[0]),len(temp[1])])
        count += 1
    pd.DataFrame(counts,columns=['TimeStamp','North','South']).to_csv('./Counts.csv',index=False)
    
def main():
    strDataFolder = './data/'
    strFileName = ['FAWNDALE_trafficnow-data (05-11-23).gz',
                   'PINE_GROVE_trafficnow-data (05-11-23).gz']
    
    interval = 60
    n = 10
    data = []
    for i in range(len(strFileName)):
        data.append(BTDF.BTgzToDF(strDataFolder+strFileName[i]))
    minTime = data[0]['TimeStamp'].min()
    maxTime = data[0]['TimeStamp'].max()
    for i in range(len(data)):
        minTime = min(minTime,data[i]['TimeStamp'].min())
        maxTime = max(maxTime,data[i]['TimeStamp'].max())

    temq = minTime + interval * n * 48    
    temo = temq + interval * n * 6 * 6

    print('Testing Dictionary Implementation of Count Occurances')
    temp = time.time()
    testDictionary(data,temq,temo,interval,n)
    dictTime = time.time()-temp
    print('Dictionary:\t' + str(dictTime),end='\n\n')

    print('Testing DataFrame Implementation of Count Occurances')
    temp = time.time()
    testDataFrame(data,temq,temo,interval,n)
    dfTime = time.time() - temp
    print('DataFrame:\t'+str(dfTime),end='\n\n')

    print('Testing Compute Travel Times')
    testTravelTimes(data,minTime,maxTime,interval,n*6)
    print('\n')

    print('Testing Count Travel Times')
    testCountTravels(data,minTime,maxTime,interval,n*6)
    print('\n')
                    
if __name__ == '__main__':
    print('Running...')
    main()
    print('DictionaryDataFrameTesting.py')



        
        
