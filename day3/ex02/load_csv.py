import pandas as pd


def load(path: str) -> pd.array:
    """Loads a csv as a pandas dataframe.
     Returns None if any error happens"""
    try:
        data = pd.read_csv(path)
        print(f"Loaded {path} with dimentions {data.shape}")
        return data
    except BaseException:
        return None


# from load_csv import load
# print(load("life_expectancy_years.csv"))
