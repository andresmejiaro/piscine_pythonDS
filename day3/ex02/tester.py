#%%
from load_csv import load
import plotly.express as px
import pandas as pd


data=pd.read_csv("~/pythonfds/day3/ex02/population_total.csv")

#%%
data=data.melt(id_vars=["country"], var_name = "Year", value_name="population")

data["population"] = data["population"].apply(lambda x: float(x[:-1])*1000000)

data=data[data["country"].isin( ["Spain","Colombia"])]

fig = px.line(data, x="Year", y="population", color="country", 
              title="Life Expectancy over Years by Country",
              labels={"life_expectancy": "Life Expectancy", "Year": "Year"})



fig.show()
# %%

