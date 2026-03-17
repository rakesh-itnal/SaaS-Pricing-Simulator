import pandas as pd

def load_data(path):

    df = pd.read_csv(path)

    print("Usage data loaded")

    return df