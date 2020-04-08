# my_lambdata/my_mod.py

# Check data frame for nulls:

import pandas as pd
import numpy as np

# python setup.py sdist bdist_wheel (build the actual package)
# twine upload --repository-url https://test.pypi.org/legacy/ dist/* --skip-existing



def dock_tester(a):
    a = a + a
    print a

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
    numeric_features = train_features.select_dtypes(include='number').columns.tolist()

    # Get a series with the cardinality of the nonnumeric features
    cardinality = train_features.select_dtypes(exclude='number').nunique()

    # Get a list of all categorical features with cardinality <= 50
    categorical_features = cardinality[cardinality <= 50].index.tolist()

    # Combine the lists
    features = numeric_features + categorical_features

    return features

# Class that performs some common model preparation tasks


class Model_Prep():
    """
    Takes a pd.DataFrame and drops a target variable
    by passing in the column name.
    Takes a pd.DataFrame and returns columns with only
    numeric data types.
    Takes a pd.DataFrame and returns columns with 
    cardinality of less than 50.
    Takes a pd.DataFrame and combines columns with
    numeric features and low cardinality features.
    """

    def __init__(self, dataframe, target=None):
        self.dataframe = dataframe
        self.target = target

    # Drop target variable in a dataframe
    def drop_target(self):
        train_features = self.dataframe.drop(columns=[self.target])
        return train_features

    # Get a list of the numeric features
    def numeric_features(self):
        numeric_features = self.dataframe.select_dtypes(include='number').columns.tolist()
        return numeric_features

    # Get a list of all categorical features with cardinality <= 50
    def cardinality(self):
        cardinality = self.dataframe.select_dtypes(exclude='number').nunique()
        categorical_features = cardinality[cardinality <= 50].index.tolist()
        return categorical_features

    # Combine list of categorical/numeric features
    def numeric_cat_combine(self):
        numeric_features = self.dataframe.select_dtypes(include='number').columns.tolist()
        cardinality = self.dataframe.select_dtypes(exclude='number').nunique()
        categorical_features = cardinality[cardinality <= 50].index.tolist()
        features = numeric_features + categorical_features
        return features


if __name__ == "__main__":

    df = pd.read_csv('https://raw.githubusercontent.com/KyleTy1er/Build-Week-Unit-2/master/fighters_df.csv', index_col=0)
    df_test = Model_Prep(df, 'is_winner')

    display_mod()
    print (df_test.drop_target())
    print (df_test.numeric_features())
    print (df_test.cardinality())
    print (df_test.numeric_features())
    print (df_test.numeric_cat_combine())
