import pandas as pd
import plotly
import plotly_express as px
from plotly.subplots import make_subplots

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

    fig2 = px.line(dataframe2, 
        y=ylabel2,
        labels=stdlabels
    ).update_traces(line_color='red')

    # Move fig2's y-axis to seconday position
    fig2.update_traces(yaxis="y2")

    # Combine figures and set axis labels
    subfig.add_traces(fig1.data + fig2.data)
    subfig.layout.xaxis.title="Datum"
    subfig.layout.yaxis.title=f"{ylabel1} (blå)"
    subfig.layout.yaxis2.title=f"{ylabel2} (röd)"

    # Return figure object
    return subfig
