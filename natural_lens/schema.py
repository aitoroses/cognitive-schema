import psycopg2
import pandas as pd
import os

def download_schema(dbname, user, password, host, port):
    """Connect to the database and download the schema and sample data."""
    print("Establishing connection to the database.")
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connection established.")

    # Query for schema
    schema_query = """
    SELECT
        table_name,
        column_name,
        data_type
    FROM
        information_schema.columns
    WHERE
        table_schema = 'public';
    """

    # Fetch the schema
    print("Fetching the schema.")
    schema_df = pd.read_sql(schema_query, conn)
    print("Schema fetched successfully.")

    # Fetch sample data for each table
    sample_data = {}
    total_tables = len(schema_df['table_name'].unique())
    for index, table in enumerate(schema_df['table_name'].unique(), start=1):
        print(f"Fetching sample data for table: {table} ({index}/{total_tables})")
        sample_query = f"SELECT * FROM {table} LIMIT 1000;"
        sample_data[table] = pd.read_sql(sample_query, conn)
        print(f"Sample data for table {table} fetched successfully. Remaining: {total_tables - index}")

    # Close the connection
    print("Closing the connection.")
    conn.close()
    print("Connection closed.")

    # Ensure the directories exist
    os.makedirs("data", exist_ok=True)

    # Save schema and sample data to CSV files
    print("Saving schema and sample data to CSV files.")
    schema_df.to_csv("schema.csv", index=False)
    for table, data in sample_data.items():
        data.to_csv(f"data/{table}.csv", index=False)
    print("Schema and sample data saved to CSV files successfully.")