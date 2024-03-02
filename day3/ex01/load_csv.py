import pandas as pd

def load(path: str) -> pd.array: 
    try:
        data = pd.read_csv(path)
        data.shape
        return data
    except:
        return None