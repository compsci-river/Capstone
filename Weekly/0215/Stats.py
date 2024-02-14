"""
Stats
"""

import pandas as pd
import statistics as st

def CountSenses(interval,maxTime,curDict):
    count = 0
    for key in curDict:
        if curDict[key] > maxTime-interval:
            count += 1
    return count

def CountTravels(interval,maxTime,dOne,dTwo):
    count = 0
    for key in dOne:
        if key in dTwo:
            if dOne[key] > dTwo[key] and dTwo[key] > maxTime-interval:
                count += 1
    return count

def AverageTravelTime(interval,maxTime,dOne,dTwo):
    times = []
    for key in dOne:
        if key in dTwo:
            if dOne[key] > dTwo[key] and dTwo[key] > maxTime-interval:
                times.append(dOne[key]-dTwo[key])
    if len(times) > 0:
        return st.mean(times)
    else:
        return -1

def MedianTravelTime(interval,maxTime,dOne,dTwo):
    times = []
    for key in dOne:
        if key in dTwo:
            if dOne[key] > dTwo[key] and dTwo[key] > maxTime-interval:
                times.append(dOne[key]-dTwo[key])
    if len(times) > 0:
        return st.median(times)
    else:
        return -1
