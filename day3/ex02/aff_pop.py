import plotly.express as px
from load_csv import load


def main():
    try:
        data = load("~/pythonfds/day3/ex02/population_total.csv")
        data = data.melt(id_vars=["country"], var_name="Year",
                         value_name="population")
        data["population"] = data["population"].apply(
            lambda x: float(x[:-1]) * 1000000)
        data["Year"] = data["Year"].apply(
            lambda x: int(x))
        data = data[data["country"].isin(["Spain", "Colombia"])]
        data = data[data["Year"] >= 1800][data["Year"] <= 2050]

        fig = px.line(data, x="Year", y="population", color="country",
                      title="Propulation Projections",
                      labels={"life_expectancy": "Life Expectancy",
                              "Year": "Year"})
        fig.show()
    except BaseException as e:
        print(f"Something wrong happened: {e}")


if __name__ == "__main__":
    main()
