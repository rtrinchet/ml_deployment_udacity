import pandas as pd


def read_data():
    df = pd.read_csv("data/census.csv")
    return df


def clean_data(df):
    df.columns = [c.strip() for c in df.columns]
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df


if __name__ == "__main__":
    df = read_data()
    df = clean_data(df)
    df.to_csv("data/census_clean.csv", index=None)

    for c in df.columns:
        print(f"Column:{c}")
        df[c].unique()
