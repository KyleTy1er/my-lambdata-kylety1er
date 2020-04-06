# my_lambdata/my_mod.py

import pandas as pd
import numpy as np 

# Check data frame for nulls:

def null_checker(a):
  null_columns=a.columns[a.isnull().any()]
  return a[null_columns].isnull().sum().sort_values(ascending=True).head(50)


# Function to set notebook display options:

def display_mod():
  pd.set_option('display.max_columns', None)
  pd.set_option('display.max_rows', None)
  pd.options.display.max_seq_items = None

