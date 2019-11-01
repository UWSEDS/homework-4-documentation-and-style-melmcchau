"""
This module contains a number of functions that can be used to test elements
of a csv(from a chosen_url) and a list of column types.

The last function calls the "read in data" function as well as all of the tests.
The last function is called by ther run_testing.py function.

"""
import pandas as pd

# import data from Buzzfeed Data GitHub on Top 2018 Fake New Articles
def readindata(chosen_columns, chosen_url):
    """Reads in the given data from the user"""
    return pd.read_csv(chosen_url, usecols=chosen_columns)

# Define Test Funtions (from Homework 2)
def checkcolumnstest(chosen_columns, chosen_df):
    """Checks columns to make sure that they match the specified input"""
    if not all([item in chosen_columns for item in chosen_df.columns]):
        raise ValueError('Columns do not match')

def checktypestest(chosen_df):
    """Checks column types to make sure that they are all the same"""
    for i in chosen_df:
        if not chosen_df.dtypes[1] == chosen_df.dtypes[i]:
            raise ValueError('Types do not match')

def checkrowstest(chosen_df):
    """Checks to make sure there is at least one row"""
    if not chosen_df.shape[0] >= 1:
        raise ValueError('Less than 10 rows')

def checkfornan(chosen_df):
    """Checks for any NaN cells in the dataframe"""
    if not chosen_df.isnull().values.any():
        raise ValueError('NaN in DataFrame')

# Run Test Functions
def test_create_dataframe(chosen_columns, chosen_url):
    """Imports data and runs required tests"""
    print("reading in data")
    chosen_df = readindata(chosen_columns, chosen_url)
    print("checking columns")
    checkcolumnstest(chosen_columns, chosen_df)
    print("checking types")
    checktypestest(chosen_df)
    print("checking for Nan")
    checkfornan(chosen_df)
    print("checking 1 row")
    checkrowstest(chosen_df)
    return True
