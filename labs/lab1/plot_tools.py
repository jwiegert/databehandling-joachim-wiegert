import pandas as pd
from pandas.core.frame import DataFrame

#import plotly
import plotly_express as px
from plotly.subplots import make_subplots

import seaborn as sns
import matplotlib.pyplot as plt

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Seaborn line plot function
def sns_line(data, xparam, yparam, xlabel, ylabel, ax):
    """
    Set settings for custom seaborn lineplots and plots
    Used for loops of subplots
    (Documentation is non-existent here, I know, didn't have the time)
    """
    ax.set(ylabel=ylabel, xlabel=xlabel)
    ax.set_xticks(list(range(0,len(data[xparam]),20)))
    ax.grid(color="lightgray")
    sns.lineplot(data=data, x=xparam, y=yparam, ax=ax)


# Plotly express function to set settings
def pxplot_twoline(dataframe1, dataframe2, ylabel1, ylabel2):
    """Plot two lines with two different y-axis in the same figure"""

    # Standard labels
    stdlabels = {"index":"Datum", "value":"Antal", "variable":""}

    # Create main figure object
    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    # Create two figure objects
    fig1 = px.line(dataframe1, 
        y=ylabel1,
        labels=stdlabels
    ).update_traces(line_color='blue')

    # Move fig2's y-axis to seconday position
    fig2 = px.line(dataframe2, 
        y=ylabel2,
        labels=stdlabels
    ).update_traces(line_color='red', yaxis="y2")

    # Combine figures and set axis labels
    subfig.add_traces(fig1.data + fig2.data)
    subfig.layout.xaxis.title="Datum"
    subfig.layout.yaxis.title=f"{ylabel1} (blå)"
    subfig.layout.yaxis2.title=f"{ylabel2} (röd)"

    # Return figure object
    return subfig


def weekly_totals(df, reversed=False):
    """
    Take weekly totals of time series data frames with daily data
    Indeces must be dates in datetime format
    reversed=True if time series first row is latest date
    """

    days = 7
    Nweeks = int(df.index.size / days)
    df_week = {}

    for n in range(Nweeks):
        # Extract times
        starttime = df.index[n*days].date()
        year = df.index[n*days].year
        week = df.index[n*days].week

        # Add to dictionary
        if reversed == True:
            df_week[f"{year} v.{week}"] = \
                df.loc[starttime:starttime - relativedelta(days=days)].sum()
        else:
            df_week[f"{year} v.{week}"] = \
                df.loc[starttime:starttime + relativedelta(days=days)].sum()

    # Save to new dataframe
    df_week = pd.DataFrame(df_week).transpose()
    
    return df_week

def weekly_averages(df: DataFrame, column: str, datecolumn: str) -> DataFrame:
    """Takes average daily value on a weekly bases for time series data frames"""

    # Create empty dateframe
    df_week = pd.DataFrame()

    for value in df[column].unique():
        df2 = df[df[column] == value].resample(
            pd.Timedelta(value=7,unit="days"), on=datecolumn, axis="rows").mean()
        df_week = pd.concat([df_week,df2], axis="rows")

    return df_week