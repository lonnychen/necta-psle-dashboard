#feature_extraction.py

####################
#Libraries
#Data handling
import numpy as np
import pandas as pd
#Strings
import re
#Calculate km from difference between lat/lon coordinates
from math import radians, sin, cos, acos
####################

def from_list_extract_total(df, source_dest_pair, i_start, i_num):
    '''From the specified elements of a list, calculate a new total'''
    df[source_dest_pair[1]] = df[source_dest_pair[0]].apply(lambda x : np.sum(x[i_start:(i_start+i_num)]))
    return df

def from_list_extract_total_multiple(df, source_dest_pairs, i_start, i_num):
    '''Calls extract_list_total for each tuple in source_dest_pairs'''
    for pair in source_dest_pairs:
        df = from_list_extract_total(df, pair, i_start, i_num)
    return df

def extract_rate(df, rate_tuple):
    '''Calculates rate from tuple of: numerator / denominator = rate'''
    df[rate_tuple[2]] = df[rate_tuple[0]] / df[rate_tuple[1]]
    return df

def extract_rate_multiple(df, rate_tuples):
    '''Calls extract_rate for each tuple in rate_tuples'''
    for rate_tuple in rate_tuples:
        df = extract_rate(df, rate_tuple)
    return df

def calc_pbr_std7(df_row, pbr_cols):
    """Calculate average Pupil-to-Book Ratio (PBR) for standard seven PSLE subjects (6)
    Parameters:
        df_row (Series): DataFrame row with specific Texbook data columns
        pbr_cols (list): PBR columns
    Returns:
        Average of PBRs if all > 0, else NA (float)"""
    
    pbr_list = list()
    for col in pbr_cols:
        if df_row[col] > 0:
            pbr_list.append(df_row[col])
        else:
            return np.nan
    return np.mean(pbr_list)

def calc_bpr_std7(df_row, pupils_col, books_cols):
    """Calculate average Book-to-Pupil Ratio (BPR) for standard seven PSLE subjects (6)
    Parameters:
        df_row (Series): DataFrame row with specific Texbook data columns
        pupils_col (string): pupil column
        books_cols (list): books columns
    Returns:
        Average of BPRs if pupils > 0, else NA (float)"""
    
    bpr_list = list()
    if df_row[pupils_col] > 0:
        for col in books_cols:
            bpr_list.append(df_row[col] / df_row[pupils_col])
    else:
        return np.nan
    return np.mean(bpr_list)

def calc_ages_mean(x):
    '''Calculate ages mean based on per-age/gender student counts data for one school
    Notes:
        Assumes Below 6 = 5, Above 13 = 14 (minimal SD)
    
    Parameters:
        x (Series): DataFrame row of TAMISEMI ages data
    Returns:
        Mean of student ages
    '''
    student_ages = list()
    for col in x.index:
        if col.startswith('Below'): #boys and girls
            m = re.search('^Below\s+(\d+)', col)
            age = int(m[1]) - 1
            student_ages += [age] * x[col] #value (age) * value_count (#students)
        elif col.startswith('Above'):
            m = re.search('^Above\s+(\d+)', col)
            age = int(m[1]) + 1
            student_ages += [age] * x[col]
        elif col[0].isdigit():
            m = re.search('^(\d+)', col)
            age = int(m[1])
            student_ages += [age] * x[col]
    if student_ages:
        return np.mean(student_ages)
    else:
        return np.nan

def calc_d_km(p1, p2):
    '''Calculates distance between two coordinate points (latitude, longitude) in kilometers
    Parameters:
        p1 (tuple of two floats): coordinate points
        p2 (tuple of two floats): coordinate points
    Returns:
        Distance (float) between two points in kilometers
    '''
    
    p1_lat = radians(p1[0]) #latitude
    p1_lon = radians(p1[1]) #longitude
    p2_lat = radians(p2[0]) #latitude
    p2_lon = radians(p2[1]) #longitude
    
    #Ref: https://www.askpython.com/python/examples/find-distance-between-two-geo-locations
    acos_input = sin(p1_lat)*sin(p2_lat) + cos(p1_lat)*cos(p2_lat)*cos(p1_lon - p2_lon)
    if acos_input < -1 or acos_input > 1:
        return np.nan #in case else "ValueError: math domain error" upon acos(...)
    d = 6371.01 * acos(acos_input)
    return d #Update: okay to return 0

def find_closest_d_km(p, col, s_p):
    '''Finds closest distance between one coordinate point (latitude, longitude) and a Series of other coordinate points
    Notes:
        Exhaustive O**2 search!
    Parameters:
        p (Series containing index and tuple of two floats): coordinate points
        col (string): name of series of tuple
        s_p (Series of tuples of two floats): coordinate points to compare p to
    Returns:
        Tuple of index (for cross-checking) and distance (float) between p and closest coordinate in s_p in kilometers
    '''
    
    #Don't compare with itself, only "others"!
    s_p_others = s_p.drop(labels=p.name)
    
    s_d = s_p_others.apply(calc_d_km, args=(p[col],))
    return s_d.idxmin(), s_d.min()

def extract_context(council_name):
    '''Returns urban or rural depending on end of council name
    Parameters:
        council_name (string): name of council
    Returns:
        'urban' if these endings, else 'rural':
            - TC - Town Council
            - MC - Municipal Council
            - CC - City Council'''
    
    if (council_name.endswith('TC') or council_name.endswith('MC') or council_name.endswith('CC')):
        return 'urban'
    else:
        return 'rural'
