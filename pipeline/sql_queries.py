import pandas as pd

from pipeline.database import create_connection


def run_query(query):
    """
    Execute SQL query and return DataFrame.
    """

    conn = create_connection()

    df = pd.read_sql(query, conn)

    conn.close()

    return df