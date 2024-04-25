import sqlite3 # Import SQLite library for database operations
import pandas as pd # Import Pandas library for data manipulation


def read_business_csv():
    """
        Reads data from a CSV file, saves it to a SQLite database table,
        and displays the DataFrame.

        :return: None
        """
    try:
        # Path to the CSV file
        file_path = "business.csv"
        # Connect to SQLite database
        conn = sqlite3.connect('myDatabase.db')

        # Read the CSV file into a DataFrame
        business_df = pd.read_csv(file_path)

        # Display the DataFrame
        print("Business DataFrame:")
        print(business_df)

        try:
            # Save the DataFrame to SQLite table
            business_df.to_sql('business', conn, if_exists='replace', index=False)
            print("Data saved to SQLite table 'business' successfully.")
        except Exception as e:
            print("An error occurred while saving to SQLite table:", e)

    except FileNotFoundError:
        print(f"File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
