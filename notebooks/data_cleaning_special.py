#data_cleaning_special.py

####################
#Libraries
#Data handling
import numpy as np
import pandas as pd
####################

####################
#(ii) Data, column values
####################

def capitalize_salaam(df):
    '''Replace Dar es salaam with Dar es Salaam'''
    return df.replace(to_replace='Dar es salaam', value = 'Dar es Salaam', regex = True)

def format_necta_id(df, col):
    '''Remove '-' in TAMISEMI's NECTA ID to match NECTA'''
    df[col] = df[col].apply(lambda x : ''.join(str(x).split('-')))
    df[col] = df[col].replace('nan', np.nan) #undo above apply which un-NaNs the NaNs
    return df

def parse_mwater_gps_to_latlon(df, lat_col, lon_col):
    '''Parses latitude and longitude values from mWater GPS Location format'''
    df[lat_col] = df.apply(lambda x: float(x['GPS Location'].replace('[', ',').split(',')[3]), axis=1)
    df[lon_col] = df.apply(lambda x: float(x['GPS Location'].replace('[', ',').split(',')[2]), axis=1)
    return df

####################
#Other data cleaning
####################

def assign_grade(marks: int):
    '''Assigns grade based on range of mark
    Parameters:
        marks (int): mark from 0 to 300
    Returns:
        Grade from A-E (str)
    '''
    if marks < 60.5:
        return 'E'
    elif marks < 120.5:
        return 'D'
    elif marks < 180.5:
        return 'C'
    elif marks < 240.5:
        return 'B'
    else:
        return 'A'
    
def compare_grade(df, grade, marks):
    '''Compares the expected grade assignment with marks'''
    assert (df[grade] == df[marks].apply(assign_grade)).all(), 'Found mismatch in grade assignment!'

