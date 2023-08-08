#data_cleaning.py

####################
#Libraries
#Data handling
import numpy as np
import pandas as pd
#Strings
from ast import literal_eval
####################

####################
#(i) Data types
####################

def convert_dtypes(df):
    '''From Pandas: Convert columns to the best possible dtypes using dtypes supporting pd.NA.'''
    return df.convert_dtypes()

def convert_string_to_list(df, cols):
    '''Convert DF columns read from CSV as string back into lists'''
    for col in cols:
        df[col] = df[col].apply(literal_eval)
    return df

def convert_float_to_int(df, cols):
    '''Converts data type to Int64 with float rounding'''
    df[cols] = df[cols].round().astype('Int64')
    return df

####################
#(ii) Data, column values
####################

def rename_column(df, old, new):
    '''Rename a DF column from old to new names'''
    return df.rename(columns={old: new})

def set_index(df, index):
    '''Puts index column as new DF index'''
    return df.set_index(index)

def is_diff_nans_equal(df, col1, col2, col_diff):
    '''col_diff is True when col1 and col2 differ, and False when they do not including both NaNs'''
    df[col_diff] = ((df[col1] != df[col2]) & ~(df[col1].isna() & df[col2].isna()))
    return df

def do_manual_fixes(df, col, dict_fixes):
    '''Manually fixes specific values in a DF where dict_fixes[idx] = value'''
    #Copy to a 'fix' column
    col_fix = col + ' fix'
    df[col_fix] = df[col]
    
    #Make the fix in the 'fix' column
    for key in dict_fixes.keys():
        df.at[key, col_fix] = dict_fixes[key]
    
    #Flag all fixes in a 'is_fixed' column
    col_is_fixed = col + ' is_fixed'
    df = is_diff_nans_equal(df, col, col_fix, col_is_fixed)
        
    return df

def compare_cols(df, col1, col2):
    '''Compares two columns for equality including no NaNs'''
    assert (df[col1] == df[col2]).all(), 'Found mismatch!'

####################
#(iii) Duplicates
####################

def count_duplicates(df, col):
    '''Returns count of non-NA duplicated values in col'''
    return df[col].dropna().duplicated().sum()

def drop_duplicates_all(df, col):
    '''Drops all cases of duplicates from specified column'''
    return df.drop_duplicates(subset=[col], keep=False)

####################
#(iv) Missing data
####################

def count_missing_rows(df, mode='total'):
    '''Returns count of rows with any missing values by total, columns, or specified column only'''
    if mode == 'total':
        return df.isna().any(axis=1).sum()
    elif mode == 'by_cols':
        return df.isna().sum()
    else:
        return df[mode].isna().sum()

def write_missing_rows(df, path):
    '''Write DF rows with any missing values to a CSV at path'''
    df[df.isna().any(axis=1)].to_csv(path)
    
def drop_missing_rows(df):
    '''Drop DF rows with any missing values'''
    return df.dropna(axis=0, how='any')

def fillna_cols(df, cols, value):
    '''Fill NA values in list of cols with specified value'''
    for col in cols:
        df[col] = df[col].fillna(value)
    return df

def fillna_not_fixed(df, cols):
    '''Fill NA values in fix columns from original column'''
    for col in cols:
        df[f'{col} fix'] = df[f'{col} fix'].fillna(df[col])
    return df

####################
#(v) Drop unneeded columns
####################

def drop_columns(df, cols):
    '''Drop DF columns from list'''
    return df.drop(cols, axis=1)

####################
#Other data cleaning
####################

def compare_list_total(df, list_total, total):
    '''Compares the total of a list of numbers versus a reference total'''
    assert (df[list_total].apply(np.sum) == df[total]).all(), 'Found mismatch in list total!'
    
def merge_outer_split_results(df, left_cols, right_cols):
    '''Splits both, left, right results of an OUTER JOIN (Pandas merge)'''
    df_both = df[df['_merge'] == 'both'].drop('_merge', axis=1)
    df_left = df[df['_merge'] == 'left_only'].drop('_merge', axis=1)[left_cols]
    df_right = df[df['_merge'] == 'right_only'].drop('_merge', axis=1)[right_cols]
    return df_both, df_left, df_right

