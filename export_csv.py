import sqlite3 # Import SQLite library for database operations
import csv # Import CSV library for file operations


def read_data_from_sqlite(database_file, table_name, csv_file):
    """
       Reads data from a SQLite database table and exports it to a CSV file.

       :param database_file: Path to the SQLite database file.
       :param table_name: Name of the table to read data from.
       :param csv_file: Path to the CSV file to export data to.
       :return: None
       """
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # Fetch data from the table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write column headers to the CSV file
        writer.writerow([i[0] for i in cursor.description])  # Write column headers
        # Write rows of data to the CSV file
        writer.writerows(rows)

    # Print a success message
    print(f"Data successfully exported to {csv_file}")

    # Close the database connection
    conn.close()


def export_data():
    """
       Function to export data from SQLite database to a CSV file.
       """
    database_file = 'myDatabase.db'
    table_name = 'business'
    csv_file = 'business.csv'

    # Read data from SQLite database
    data = read_data_from_sqlite(database_file, table_name, csv_file)



