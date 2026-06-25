import pandas as pd


def load_matches(filepath):
    """
    Load IPL matches dataset.
    """
    return pd.read_csv(filepath)


def load_deliveries(filepath):
    """
    Load IPL deliveries dataset.
    """
    return pd.read_csv(filepath)


if __name__ == "__main__":
    matches = load_matches("data/raw/matches.csv")
    deliveries = load_deliveries("data/raw/deliveries.csv")

    print("Matches Shape:", matches.shape)
    print("Deliveries Shape:", deliveries.shape)