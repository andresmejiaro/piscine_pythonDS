# %%
from load_csv import load
import plotly.express as px


def main():
    """
    loads life_expectancy_years.csv and plots Spain's Life expectancy
    projections
    """
    try:
        data = load("life_expectancy_years.csv")

        data = data.melt(
            id_vars=["country"],
            var_name="Year",
            value_name="life_expectancy")

        data = data[data["country"] == "Spain"]

        fig = px.line(data_frame=data,
                      x=data["Year"],
                      y=data["life_expectancy"],
                      title="Spain Life Expectancy Projections",
                      labels={"Year": "Year",
                              "life_expectancy": "Life Expectancy"})
        fig.show()

    except BaseException as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
