# %%
from load_csv import load
import plotly.express as px
import pandas as pd


data = pd.read_csv(
    "/home/andres/pythonfds/day3/ex03/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

# %%
data = data.melt(
    id_vars=["country"],
    var_name="Year",
    value_name="life expectancy")


data = data[data["country"].isin(["Spain", "Colombia"])]

fig = px.line(data, x="Year", y="life expectancy", color="country",
              title="Life Expectancy over Years by Country",
              labels={"life_expectancy": "Life Expectancy", "Year": "Year"})


fig.show()
# %%
