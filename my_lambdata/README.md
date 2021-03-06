

# Model Prep: toolkit for preparing a Pandas Dataframe for use in a predictive model:
[![PyPI Latest Release](https://test.pypi.org/project/my-lambdata-kylety1er/8.0/)
[![License](https://github.com/KyleTy1er/my-lambdata-kylety1er/blob/master/my_lambdata/LICENSE)

## What is it?

**Model Prep** is a Python package that provides some quick and commonly used methods for preparing a Pandas Dataframe.

## Main Features
Model prep can do these things:

  - Quickly list the column names beside the sum of null values in that column.
  - Drop a target variable (column) from dataframe.
  - Remove high cardinality columns from dataframe.
  - Separate and return only numeric columns from dataframe.
  - Return "low" cardinality columns and numeric features, then combine into one
    set of features to be used in a model.

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/KyleTy1er/my-lambdata-kylety1er/tree/master/my_lambdata


## Dependencies
- [NumPy](https://www.numpy.org)
- [Pandas](https://pandas.pydata.org/)

