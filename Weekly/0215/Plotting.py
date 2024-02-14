"""
Stat Plot Creation

"""

import pandas as pd
import matplotlib as plt
import seaborn as sns
import ProcessBluetoothData as BTDF
import DataHandling as dh
import Stats as st
import datetime as dt

def plotFrequency(path,interval,name):
    data = BTDF.BTgzToDF(path)
    minTime = data['TimeStamp'].min()
    maxTime = data['TimeStamp'].max()
    counts = []
    dic = {}
    while minTime < maxTime:
        dic = dh.BatchUpdate(data,minTime,minTime+interval,dic)
        temp = st.CountSenses(interval,minTime+interval,dic)
        time = dt.datetime.fromtimestamp((2*minTime+interval)/2)
        counts.append([time,temp])
        minTime += interval
    df = pd.DataFrame(counts,columns=['Date','Frequency'])
    p = sns.scatterplot(x='Date',y='Frequency',data=df)
    p.set_title('Sensor Frequency '+name)
    xDates = df['Date'].dt.strftime('%b-%d').sort_values().unique()
    xTicks = [dt.datetime.strptime(x+'-2023','%b-%d-%Y') for x in xDates]
    p.set_xticks(xTicks)
    p.set_xticklabels(labels=xDates,rotation=30)
    #plt.pyplot.xticks(rotation=30)
    p.figure.savefig(name+'_SF.png')
    p.figure.clf()

def plotTravelFrequency(pOne,pTwo,interval,name):
    data = [BTDF.BTgzToDF(pOne),BTDF.BTgzToDF(pTwo)]
    minTime = min(data[0]['TimeStamp'].min(),data[1]['TimeStamp'].min())
    maxTime = max(data[0]['TimeStamp'].max(),data[1]['TimeStamp'].max())
    counts = []
    dicts = [{},{}]
    while minTime < maxTime:
        dicts = dh.SiteAlignment(data,minTime,minTime+interval,dicts)
        temp = st.CountTravels(interval,minTime+interval,dicts[0],dicts[1])
        time = dt.datetime.fromtimestamp((2*minTime+interval)/2)
        counts.append([time,temp])
        minTime += interval
    df = pd.DataFrame(counts,columns=['Date','Frequency'])
    p = sns.scatterplot(x='Date',y='Frequency',data=df)
    p.set_title('Travel Frequency '+name)
    xDates = df['Date'].dt.strftime('%b-%d').sort_values().unique()
    xTicks = [dt.datetime.strptime(x+'-2023','%b-%d-%Y') for x in xDates]
    p.set_xticks(xTicks)
    p.set_xticklabels(labels=xDates,rotation=30)
    p.figure.savefig(name+'_TF.png')
    p.figure.clf()

def plotAverageTravelTime(pOne,pTwo,interval,name):
    data = [BTDF.BTgzToDF(pOne),BTDF.BTgzToDF(pTwo)]
    minTime = min(data[0]['TimeStamp'].min(),data[1]['TimeStamp'].min())
    maxTime = max(data[0]['TimeStamp'].max(),data[1]['TimeStamp'].max())
    counts = []
    dicts = [{},{}]
    while minTime < maxTime:
        dicts = dh.SiteAlignment(data,minTime,minTime+interval,dicts)
        temp = st.AverageTravelTime(interval,minTime+interval,dicts[0],dicts[1])
        if temp > 0:
            time = dt.datetime.fromtimestamp((2*minTime+interval)/2)
            counts.append([time,temp])
        minTime += interval
    df = pd.DataFrame(counts,columns=['Date','TravelTime'])
    p = sns.scatterplot(x='Date',y='TravelTime',data=df)
    p.set_title('Average Travel Time '+name)
    xDates = df['Date'].dt.strftime('%b-%d').sort_values().unique()
    xTicks = [dt.datetime.strptime(x+'-2023','%b-%d-%Y') for x in xDates]
    p.set_xticks(xTicks)
    p.set_xticklabels(labels=xDates,rotation=30)
    p.figure.savefig(name+'_ATT.png')
    p.figure.clf()

def plotMedianTravelTime(pOne,pTwo,interval,name):
    data = [BTDF.BTgzToDF(pOne),BTDF.BTgzToDF(pTwo)]
    minTime = min(data[0]['TimeStamp'].min(),data[1]['TimeStamp'].min())
    maxTime = max(data[0]['TimeStamp'].max(),data[1]['TimeStamp'].max())
    counts = []
    dicts = [{},{}]
    while minTime < maxTime:
        dicts = dh.SiteAlignment(data,minTime,minTime+interval,dicts)
        temp = st.MedianTravelTime(interval,minTime+interval,dicts[0],dicts[1])
        if temp > 0:
            time = dt.datetime.fromtimestamp((2*minTime+interval)/2)
            counts.append([time,temp])
        minTime += interval
    df = pd.DataFrame(counts,columns=['Date','TravelTime'])
    p = sns.scatterplot(x='Date',y='TravelTime',data=df)
    p.set_title('Median Travel Time '+name)
    xDates = df['Date'].dt.strftime('%b-%d').sort_values().unique()
    xTicks = [dt.datetime.strptime(x+'-2023','%b-%d-%Y') for x in xDates]
    p.set_xticks(xTicks)
    p.set_xticklabels(labels=xDates,rotation=30)
    p.figure.savefig(name+'_MTT.png')
    p.figure.clf()

def main():
    pOne = './data/FAWNDALE_trafficnow-data (05-11-23).gz'
    pTwo = './data/PINE_GROVE_trafficnow-data (05-11-23).gz'

    interval = 900

    print('Sensor Frequency',end='\n\n')
    plotFrequency(pOne,interval,'Fawndale')
    plotFrequency(pTwo,interval,'PineGrove')
    
    print('Travel Frequency',end='\n\n')
    plotTravelFrequency(pOne,pTwo,interval,'PineGroveToFawndale')
    plotTravelFrequency(pTwo,pOne,interval,'FawndaleToPineGrove')

    print('Average Travel Time',end='\n\n')
    plotAverageTravelTime(pOne,pTwo,interval,'PineGroveToFawndale')
    plotAverageTravelTime(pTwo,pOne,interval,'FawndaleToPineGrove')

    print('Median Travel Time',end='\n\n')
    plotMedianTravelTime(pOne,pTwo,interval,'PineGroveToFawndale')
    plotMedianTravelTime(pTwo,pOne,interval,'FawndaleToPineGrove')
    

if __name__ == '__main__':
    main()
    print('Plotting')
    
