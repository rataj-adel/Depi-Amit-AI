import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import pandas as pd 


import pandas as pd
cols = [
    "roll_no", "gender", "race_ethnicity", "parental_level_of_education",
    "lunch", "test_preparation_course", "math_score", "reading_score",
    "writing_score", "science_score", "total_score", "grade"
]

df = pd.read_csv("Student_performance.csv", header=None, names=cols)

def df_summary(df):
    """Summary of dtypes, uniques, and nulls for each column"""
    summary = pd.DataFrame({
        "Dtypes": df.dtypes,
        "Num_Uniques": df.nunique(),
        "Num_Nulls": df.isnull().sum()
    })
    summary.index.name = "Column"
    return summary.__dataframe__

print(df_summary(df))

import pandas as pd

def drop_columns(df, cols_to_drop):
    """
        Drop unwanted columns from a DataFrame.
        
    Returns:
        pd.DataFrame: New dataframe without the specified columns
    """
    return df.drop(cols_to_drop, axis=1)


df_new = drop_columns(df, ['roll_no', 'lunch', 'total_score','race_ethnicity'])
print(df_new.head())

def convert_col(df, cols):
    """
    Convert selected columns to category dtype
    """
    df[cols] = df[cols].astype("category")
    return df
df_new = convert_col(df_new, ["test_preparation_course","gender","grade"])
print(df_new.dtypes)

def to_numeric(df, cols):
    if isinstance(cols, str):
        cols = [cols]
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

df_new = to_numeric(df_new, ["math_score"])
print(df_new.dtypes)
def drop_null_rows(df, cols):
    return df.dropna(subset=cols)
"""
 Drop the only row in gender col which has a null value
"""
df_new = drop_null_rows(df_new, ["grade"])

def fill_with_mode(df, cols):
    """
     fill the null Categorical values with Mode.
    """
    for col in cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

df_new = fill_with_mode(df_new, ["gender", "parental_level_of_education", "test_preparation_course"])

def fill_with_median(df, cols):
    """
     fill the nullNumerical values with Median.
    """
    for col in cols:
        df[col] = df[col].fillna(df[col].median())
    return df
df_new = fill_with_median(df_new, ["math_score", "reading_score", "writing_score", "science_score"])

print(df_new.isnull().sum())

