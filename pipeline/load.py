import os
import pandas as pd

# Project root (IPL-Analytics-Pipeline)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def save_csv(df, filename, folder="data/cleaned"):
    """
    Save DataFrame to the project folder.
    """

    save_folder = os.path.join(PROJECT_ROOT, folder)
    os.makedirs(save_folder, exist_ok=True)

    filepath = os.path.join(save_folder, filename)

    df.to_csv(filepath, index=False)

    print(f"Saved: {filepath}")