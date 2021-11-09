# Dashboard packages
from dash.dependencies import Input, Output
from dash import dcc, html
import dash

# Dataframe and plot
import pandas as pd
import plotly_express as px

# Custom modules
from load_data import StockDataLocal
from time_filtering import filter_time

################################
# Time to create our dashboard!
# =============================

# Create an object from our load data class, ie load local data
stock_data_object = StockDataLocal()

# Drop down menu settings
# A list of companies for a dropdown menu (in dcc.Dropdown)
symbol_dict = dict(AAPL="Apple", NVDA="Nvidia", TSLA="Tesla", IBM="IBM")

stock_options_dropdown = [{
    "label": name, 
    "value": symbol} 
    for symbol, name in symbol_dict.items()]

df_dict = {symbol: stock_data_object.stock_dataframe(symbol)
    for symbol in symbol_dict}

# OHLC options : ie open high low close-options
# This choses which value to plot, the close time value or open time value etc.
# The columns in the data files are:
# [timestamp,open,high,low,close,volume]
# In the plot, we change which column is plotted with y=ohlc
ohlc_options = [{"label": option.capitalize(), "value": option} 
                for option in ["open", "high", "low", "close"]]


# Settings for time slider, slider marks must be a dict
# value=2 sets default value, which here is 1month
slider_marks = {i: mark for i,mark in enumerate(
    ["1 day", "1 week", "1 month", "3 months", "1 year", "5 years", "Max"]
)}

# Create a dash object called app
app = dash.Dash(__name__) # run __name__ to get __main__

# Define the layout for our "app"
# html.H1 = header 1, main title
# html.H2 = header 2, sub title
# html.P = paragraph
# dropdown creates a dropdown manue, id is it's name (for later), value is
# its default value. Options is a list of what you can chose.
# So value='' gives the default value for each dcc.
# The objects in app.layout ends up on the page in the order we have them written here
app.layout = html.Div([

    # Title
    html.H1("Stocks viewer"),

    # Dropdown meny with title (this is "children")
    # The first object is always the child of this dash
    html.P("Choose a stock"),
    dcc.Dropdown(id='stock-picker-dropdown', className='',
        options=stock_options_dropdown,
        value='AAPL'
    ),

    # Interactive text below dropdown menu
    html.P(id = "highest-value"),
    html.P(id = "lowest-value"),
    
    dcc.RadioItems(id='ohlc-radio', className='',
        options=ohlc_options,
        value='close'
    ),

    dcc.Graph(id='stock-graph', className=''),
    
    dcc.Slider(id='time-slider', className='',
        min=0, max=6,
        step=None,
        value=2,
        marks=slider_marks
    ),

    # Stores an intermediate value on client's browser for sharing between callbacks
    # Needs a json object, see filter_df() below
    dcc.Store(id='filtered-df')
])

# Use callback decorators for extra functions

# This stores our time filtered columns in a temporary json-file
# This way we can use these data for several callback.
# In the previous version we filtered the data inside the plot function
# then we could only use it directly for the plot function
# Now we use the filtered data both for plot and for giving max/min values
@app.callback(Output("filtered-df", "data"), 
    Input("stock-picker-dropdown", "value"),
    Input("time-slider", "value")
)
def filter_df(stock, time_index):
    """Filters the dataframe and stores in intermediary for callbacks
    Returns:
        json object of filtered dataframe
    """
    # Extract stocks (see df_dict above, it uses class to extract data from csvfiles)
    dff_daily, dff_intraday = df_dict[stock]

    # intraday or daily depends on time index input (value)
    dff = dff_intraday if time_index <= 2 else dff_daily

    # Define a dictionary with days, maps 0-6 to number of days, max is not necessary
    days = {i: day for i,day in enumerate([1,7,30,90,365,5*365])}

    # This gives max instead
    dff = dff if time_index == 6 else filter_time(dff, days[time_index])

    return dff.to_json()


# Input 1 is our dropdown menu
# Output is the graph
# Input 2 is the time slider
@app.callback(
    Output("stock-graph", "figure"),
    Input("filtered-df", "data"),
    Input("stock-picker-dropdown", "value"),
    Input("ohlc-radio", "value")
)
def update_graph(json_df, stock, ohlc):
    
    # Change our temporary json file to dataframe
    dff = pd.read_json(json_df)

    # Plot figure using dff-data
    fig = px.line(dff, 
        x=dff.index, y=ohlc, 
        labels={"close":"Stock value (us-$)"}, 
        title=symbol_dict[stock]
    )

    return fig # fig object goes into output property, ie figure property


# This gives the number of the maximum and lowest value shown in the figure
@app.callback(
    Output("highest-value", "children"),
    Output("lowest-value", "children"),
    Input("filtered-df", "data"),
    Input("ohlc-radio", "value")
)
def highest_lowest_value(json_df, ohlc):

    dff = pd.read_json(json_df)

    highest_value = f"High: {dff[ohlc].max():.1f} $"
    lowest_value = f"Low: {dff[ohlc].min():.1f} $"
    
    return highest_value, lowest_value

if __name__ == "__main__":
    app.run_server(debug=True)
