#dashboard_utils.py

####################
#Libraries
#Data handling
import numpy as np
import pandas as pd
####################

def filter_df_or_all(df, col, sel_values, all_value='ALL DEFAULT'):
    '''Returns a filtered DF based on sel_values or all if all_value is present'''
    if all_value in sel_values:
        return df
    else:
        return df[df[col].isin(sel_values)]
