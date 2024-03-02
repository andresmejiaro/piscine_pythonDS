#%%
from load_csv import load
import plotly.graph_objects as go
import pandas as pd


data=load("life_expectancy_years.csv")

data=data.melt(id_vars=["country"], var_name = "Year", value_name="life_expentancy")

data=data[data["country"] == "Spain"]

fig = go.Figure(data=go.Scatter(x=data["Year"], y=data["life_expentancy"], mode='lines'))

fig.update_layout(title = "Life Expectancy", xaxis_title = "Year", yaxis_title = "Life Expectancy")


fig.show()
# %%

