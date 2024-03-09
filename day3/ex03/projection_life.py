import plotly.express as px
import pandas as pd
from load_csv import load


def main():
    gdp = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    gdp = gdp.melt(
        id_vars=["country"],
        var_name="Year",
        value_name="gdp per capita")
    gdp["Year"] = gdp["Year"].apply(
        lambda x: int(x))
    gdp = gdp[gdp["Year"] == 1900]

    life_exp = load(
        "life_expectancy_years.csv")
    life_exp = life_exp.melt(
        id_vars=["country"],
        var_name="Year",
        value_name="life_expectancy")
    life_exp["Year"] = life_exp["Year"].apply(
        lambda x: int(x))
    life_exp = life_exp[life_exp["Year"] == 1900]

    merged_data = pd.merge(gdp, life_exp, on="country")

    fig = px.scatter(merged_data, x="gdp per capita", y="life_expectancy",
                     title="Life Expectancy vs GDP per Capita in 1900",
                     labels={"life_expectancy": "Life Expectancy",
                             "Year": "Year"})
    fig.update_layout(xaxis_type='log')

    fig.show()


if __name__ == "__main__":
    main()
