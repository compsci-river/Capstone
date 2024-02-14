"""
SingleSiteSequentialProcessing

River Sheppard
"""



import pandas as pd
import BTgzToDF as BTgz


"""
BatchUpdate(): runs through a Pandas DataFrame adding to/updating the
    curDictionary.
"""
def BatchUpdate(data,startTime,endTime, curDictionary):
    df = data.loc[(data['TimeStamp'] >= startTime) & (data['TimeStamp'] < endTime)]
    for index, row in df.iterrows():
        curDictionary[row['MAC']] = row['TimeStamp']
    return curDictionary

"""
Test
"""

def main():
    strDataFolder = './data/'
    strFileName = 'FAWNDALE_trafficnow-data (05-11-23).gz'
    strPath = strDataFolder + strFileName
    interval = 600

    data = BTgz.BTgzToDF(strPath)
    minTime = data['TimeStamp'].min()
    maxTime = data['TimeStamp'].max()
    curDictionary = {}
    while minTime < maxTime:
        curDictionary = BatchUpdate(data, minTime, minTime+interval, curDictionary)
        minTime += interval
    print(len(curDictionary))
    

if __name__ == "__main__":
    main()
    print("SingleSiteSequentialProcessing - Main.")
