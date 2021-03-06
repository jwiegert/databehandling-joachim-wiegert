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



# Time to create our dashboard!

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
app.layout = html.Div([
    html.H1("Stocks viewer"),
    html.P("Choose a stock"),
    
    dcc.Dropdown(id='stock-picker-dropdown', className='',
        options=stock_options_dropdown,
        value='AAPL'),
    
    dcc.Graph(id='stock-graph', className=''),
    
    dcc.Slider(id='time-slider', className='',
        min=0, max=6,
        step=None,
        value=2,
        marks=slider_marks)
])

# Use callback decorator for extra functions
# Input 1 is our dropdown menu
# Output is the graph
# Input 2 is the time slider
@app.callback(
    Output("stock-graph", "figure"),
    Input("stock-picker-dropdown", "value"),
    Input("time-slider", "value")
)
def update_graph(stock, time_index):
    
    # Extract stocks (see df_dict above, it uses class to extract data from csvfiles)
    dff_daily, dff_intraday = df_dict[stock]

    # intraday or daily depends on time index input (value)
    dff = dff_intraday if time_index <= 2 else dff_daily

    # Define a dictionary with days, maps 0-6 to number of days, max is not necessary
    days = {i: day for i,day in enumerate([1,7,30,90,365,5*365])}

    # This gives max instead
    dff = dff if time_index == 6 else filter_time(dff, days[time_index])

    # Plot figure using dff-data
    fig = px.line(dff, x=dff.index, y="close", labels={"close":"Stock value (us-$)"})

    return fig # fig object goes into output property, ie figure property

if __name__ == "__main__":
    app.run_server(debug=True)
