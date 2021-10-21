# Useful data handling functions

import pandas as pd
import seaborn as sns

def extract_nan_columns(df):
    """
    Extract all columns containing NaNs
    - Input: a dataframe
    - Output: a dataframe with only NaN-columns and a dataframe with number if NaNs
              per column.
    - Figure: plots these columns
    """
    # Extract all columns with NaN
    df_nan = df[df.columns[df.isna().any() == True]]
    # Save number of Nans
    Nnans = df_nan.isna().sum()
    # Put number of Nans in a dataframe (reset index and remove redundant index column)
    Nnans = pd.DataFrame(
        {"Column names":Nnans.index, "Number of NaNs":Nnans}).reset_index(drop=True)
    # Plot
    sns.barplot(data=Nnans, x="Column names", y="Number of NaNs")
    # Return data
    return df_nan, Nnans
