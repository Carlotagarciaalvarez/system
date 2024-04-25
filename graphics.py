import sqlite3  # Import SQLite library for database operations
import pandas as pd  # Import Pandas library for data manipulation
import matplotlib.pyplot as plt  # Import Matplotlib library for data visualization


def plot_graphic():
    """
     Reads data from a SQLite database table, plots lines using the data,
     and displays the plot.

     :return: None
     """
    # Connect to the SQLite database
    conn = sqlite3.connect('myDatabase.db')

    # Read the data into a DataFrame
    query = "SELECT * FROM business"
    df = pd.read_sql_query(query, conn)

    # Close the connection
    conn.close()

    # Plotting the data with a specified size
    plt.figure(figsize=(8, 6))

    # Plot line using 'x' and 'y'
    plt.plot(df['x'], df['y'], label='Line using x and y', color='blue')

    # Plot another line using 'x' and 'z'
    plt.plot(df['x'], df['z'], label='Line using x and z', color='red')

    plt.xlabel('x')
    plt.ylabel('y/z')
    plt.title('Lines Plot of x vs y and x vs z')
    plt.legend()
    plt.grid(True)
    plt.show()
