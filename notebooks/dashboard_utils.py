#dashboard_utils.py

####################
#Libraries
#Data handling
import numpy as np
import pandas as pd

#Strings
import re
####################

def filter_df_or_all(df, col, sel_values, all_value='ALL DEFAULT'):
    '''Returns a filtered DF based on sel_values or all if all_value is present'''
    if all_value in sel_values:
        return df
    else:
        return df[df[col].isin(sel_values)]

def convert_council_name(council_name):
    '''Converts council name based on suffix'''
    m = re.search('(.*)\s+(TC|MC|CC)', council_name)
    if m != None:
        if m[2] == 'TC':
            return f'{m[1]} Town'
        elif m[2] == 'MC':
            return f'{m[1]} Municipality'
        elif m[2] == 'CC':
            return f'{m[1]} City'
    else:
        return f'{council_name} District'
