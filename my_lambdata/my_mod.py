# my_lambdata/my_mod.py

# Check data frame for nulls:

import pandas as pd
import numpy as np

def null_checker(a):
  null_columns=a.columns[a.isnull().any()]
  return a[null_columns].isnull().sum().sort_values(ascending=True).head(50)


# Function to set notebook display options:

def display_mod():
  pd.set_option('display.max_columns', None)
  pd.set_option('display.max_rows', None)
  pd.options.display.max_seq_items = None


# Function to retain numeric features while dropping high cardinality features and the target variable:

def feature_keeper(dataframe, target):
    # Get a dataframe with all train columns except the target
    train_features = dataframe.drop(columns=[target])

    # Get a list of the numeric features
    numeric_features = train_features.select_dtypes(include='number').columns.tolist()

    # Get a series with the cardinality of the nonnumeric features
    cardinality = train_features.select_dtypes(exclude='number').nunique()

    # Get a list of all categorical features with cardinality <= 50
    categorical_features = cardinality[cardinality <= 50].index.tolist()

    # Combine the lists 
    features = numeric_features + categorical_features

    return features

