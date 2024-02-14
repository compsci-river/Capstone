"""
ProcessBluetoothData.py

Author: Doug Galarus

Last Updated: 2024-01-16
"""

import gzip
import pandas as pd
import io 
import hashlib


"""
BTgzToDF(): reads .gz file containing Bluetooth reads and returns Pandas DataFrame.

strPath is a string containing the path to the .gz file

returns a Pandas DataFrame containing the data
"""
def BTgzToDF(strPath):
    # Open the .gz archive and read the contents into a string.
    with gzip.open(strPath, 'rt') as f:
        strData = f.read()
    
    # Extract the relevant sections.
    sections = strData.split('[LOG]')[0].split('[')
    # BT data
    btcapt = sections[2].split(']')[1].strip()
    # BTLE data
    btlecapt = sections[4].split(']')[1].strip()
    
    # Read the BT data into a DataFrame.
    df_btcapt = pd.read_csv(io.StringIO("TimeStamp,OUI,MAC,h4,RSSI\n" + btcapt), sep=",")
    # Add column indicating type = BTCAPT
    df_btcapt["type"] = "BTCAPT"
    
    # Read the BTLE data into a DataFrame.
    df_btlecapt = pd.read_csv(io.StringIO("TimeStamp,OUI,MAC,h4,RSSI\n" + btlecapt), sep=",")
    # Add column indicating type = BTCAPT
    df_btlecapt["type"] = "BTLECAPT"
    
    # Concatentate the two DataFrames into a single DataFrame.
    df_all = pd.concat([df_btcapt,df_btlecapt])
    
    # Add column containing MD5 hash of MAC addresses.
    df_all['md5'] = [hashlib.md5(val.encode('UTF-8')).hexdigest() for val in df_all['MAC']]
    
    # Sort by TimeStamp and then the md5 hash.
    df_all = df_all.sort_values(["TimeStamp","md5"]).reset_index(drop=True)
    
    # Return the resulting DataFrame.
    return df_all


"""
Test/Demo function main()
"""
def main():
    strDataFolder = './data/'
    
    strFileName = 'FAWNDALE_trafficnow-data (05-11-23).gz'
    strPath = strDataFolder + strFileName
    print('PROCESSING: ' + strPath)
    dfFawndale = BTgzToDF(strPath)
    print('Number of records: ' + str(len(dfFawndale)))
    
    strFileName = 'PINE_GROVE_trafficnow-data (05-11-23).gz'
    strPath = strDataFolder + strFileName
    print('PROCESSING: ' + strPath)
    dfPineGrove = BTgzToDF(strPath)
    print('Number of records: ' + str(len(dfPineGrove)))
    

# Run main() if the script is called stand-alone.
if __name__ == "__main__":
    main()
