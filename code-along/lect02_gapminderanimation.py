import plotly_express as px

gapminder = px.data.gapminder()


# Actually a scatterplot
# This plots animation
fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp",
    size="pop", color="country", size_max=50, log_x=True, animation_frame="year",
    range_x=[1e2,1e5], range_y=[25,90])

fig.show()
