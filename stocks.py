import sqlite3
import pandas as pd
import yfinance as yf # pip install pandas yfinance

# Function to establish connection to SQLite database
def connect_to_sqlite():
    try:
        connection = sqlite3.connect('stock_data.db')
        print('Connected to SQLite database')
        return connection
    except sqlite3.Error as e:
        print(f"Error while connecting to SQLite: {e}")
        return None

# Function to create table in SQLite database
def create_table(connection):
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS stock_data (
            symbol VARCHAR(10) NOT NULL,
            date DATE NOT NULL,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume INT,
            PRIMARY KEY (symbol, date)
        )
        """
        cursor.execute(create_table_query)
        print('Table created successfully')
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error while creating table: {e}")

# Function to insert stock data into SQLite database
def insert_data(connection, data):
    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT OR IGNORE INTO stock_data (symbol, date, open, high, low, close, volume)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.executemany(insert_query, data)
        connection.commit()
        print('Data inserted successfully')
    except sqlite3.Error as e:
        print(f"Error while inserting data: {e}")

# Main function to fetch data from Yahoo Finance and store it in SQLite database
def main():
    # List of symbols to fetch data for
    symbols = ['AAPL', 'GOOG', 'MSFT']  # Example symbols

    # Establish connection to SQLite
    connection = connect_to_sqlite()
    if connection is None:
        return

    # Create table if not exists
    create_table(connection)

    # Fetch data from Yahoo Finance and insert into SQLite
    for symbol in symbols:
        try:
            stock_data = yf.download(symbol, start="2024-01-01", end="2024-02-27")
            stock_data.reset_index(inplace=True)
            data_to_insert = [tuple(x) for x in stock_data.to_numpy()]
            insert_data(connection, data_to_insert)
        except Exception as e:
            print(f"Error fetching data for symbol {symbol}: {e}")

    # Close SQLite connection
    connection.close()
    print('Connection to SQLite closed')

if __name__ == "__main__":
    main()
