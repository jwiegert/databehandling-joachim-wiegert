# Useful data handling functions

import pandas as pd
import seaborn as sns

def extract_nan_columns(df):
    """
    Extract all columns containing NaNs
    - Input: a dataframe
    - Output: a dataframe with only NaN-columns
    - Figure: plots these columns
    """
    df_nans = df[df.columns[df.isna().any() == True]]
    sns.barplot(data=df_nans)
    return df_nans
