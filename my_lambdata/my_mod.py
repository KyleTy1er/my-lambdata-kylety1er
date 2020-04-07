# my_lambdata/my_mod.py

# Check data frame for nulls:

import pandas as pd
import numpy as np


def null_checker(a):
    # Creating a list of all columns containing a null value:
    null_columns=a.columns[a.isnull().any()]
    # Subsetting the dataframe to retain only the columns with null values
    # Summing and sorting those null values by their column from
    # least to greatest and limiting output to top 50 results
    return a[null_columns].isnull().sum().sort_values(ascending=True).head(50)


# Function to set multiple notebook display options:

def display_mod():
    # Allows output of all columns in a pd.DataFrame
    pd.set_option('display.max_columns', None)
    # Allows output of all rows in a pd.DataFrame
    pd.set_option('display.max_rows', None)
    # Allows display of full column list when using df.columns
    pd.options.display.max_seq_items = None


# Function to retain numeric/low cardinality features while
# dropping high cardinality features and the target variable:

def feature_keeper(dataframe, target):
    # Get a dataframe with all train columns except the target
    train_features = dataframe.drop(columns=[target])

    # Get a list of the numeric features
    numeric_features = train_features.select_dtypes(include='number') /
    .columns.tolist()

    # Get a series with the cardinality of the nonnumeric features
    cardinality = train_features.select_dtypes(exclude='number').nunique()

    # Get a list of all categorical features with cardinality <= 50
    categorical_features = cardinality[cardinality <= 50].index.tolist()

    # Combine the lists
    features = numeric_features + categorical_features

    return features


class 