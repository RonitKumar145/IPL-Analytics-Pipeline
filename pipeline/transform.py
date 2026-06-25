import pandas as pd


def convert_dates(df):
    """
    Convert date column to datetime.
    """
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    return df


def extract_year(df):
    """
    Extract year from date.
    """
    if "date" in df.columns:
        df["season_year"] = df["date"].dt.year

    return df


def fill_missing_city(df):
    """
    Fill missing city values with 'Unknown'.
    """
    if "city" in df.columns:
        df["city"] = df["city"].fillna("Unknown")

    return df