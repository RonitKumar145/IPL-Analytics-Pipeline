import sqlite3
import pandas as pd
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATABASE_PATH = os.path.join(PROJECT_ROOT, "ipl.db")


def create_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn


def save_to_database(df, table_name):
    conn = create_connection()

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print(f"{table_name} saved successfully.")


def read_table(table_name):
    conn = create_connection()

    df = pd.read_sql(
        f"SELECT * FROM {table_name}",
        conn
    )

    conn.close()

    return df