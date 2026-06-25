import pandas as pd


def remove_duplicates(df):
    """
    Remove duplicate rows from a DataFrame.
    """
    return df.drop_duplicates()


def missing_value_report(df):
    """
    Generate missing value summary.
    """
    report = pd.DataFrame({
        "Missing Values": df.isnull().sum(),
        "Percentage": (df.isnull().sum() / len(df) * 100).round(2)
    })

    return report.sort_values(by="Missing Values", ascending=False)


def standardize_column_names(df):
    """
    Convert column names to lowercase and replace spaces with underscores.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df