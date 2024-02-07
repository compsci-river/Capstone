"""
To CSV

River Sheppard
"""

import pandas as pd
import ProcessBluetoothData as BTDF

def GzToCSV(dFolder,fName,name):
    df = BTDF.BTgzToDF(dFolder+fName)
    df.to_csv(dFolder+name+'.csv', index=False)

def main():
    dFolder = './data/'
    fName = 'FAWNDALE_trafficnow-data (05-11-23).gz'
    name = 'Fawndale'
    GzToCSV(dFolder,fName,name)

if __name__ == '__main__':
    main()
