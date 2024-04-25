import sqlite3 # Import SQLite library for database operations


def sp_execute(sql_command):
    # Connect to SQLite database
    conn = sqlite3.connect('myDatabase.db')

    # Create a cursor object
    cursor = conn.cursor()
    cursor.execute(sql_command)

    # Commit changes and close connection
    conn.commit()
    conn.close()


def sp_query(sql_command):
    # Connect to SQLite database
    conn = sqlite3.connect('myDatabase.db')

    # Create a cursor object
    cursor = conn.cursor()
    cursor.execute(sql_command)
    rows = cursor.fetchall()

    # Display fetched data
    for row in rows:
        print(row)

    # Commit changes and close connection
    conn.commit()
    conn.close()


def create_table(table_name, columns_definition):
    """
        Creates a new table in the database if it doesn't already exist.

        :param table_name: Name of the table to be created.
        :param columns_definition: String containing the columns and their data types definition.
        """
    sql_command = f'CREATE TABLE IF NOT EXISTS {table_name} ( {columns_definition} )'
    # Executes SQL command
    sp_execute(sql_command)


def drop_table(table_name):
    """
        Drops a table from the database if it exists.

        :param table_name: Name of the table to be dropped.
        """
    sql_command = f'DROP TABLE IF EXISTS {table_name}'
    # Executes SQL command
    sp_execute(sql_command)


def insert_record(table_name, columns_definition, record_values):
    """
       Inserts a new record into the specified table.

       :param table_name: Name of the table where the record will be inserted.
       :param columns_definition: String containing the columns where values will be inserted.
       :param record_values: Values to be inserted into the table.
       """
    sql_command = f'INSERT INTO {table_name} ( {columns_definition} ) VALUES ( {record_values} )'
    # Executes SQL command
    sp_execute(sql_command)


def delete_record(table_name, columns_definition, record_values):
    """
        Deletes a record from the specified table based on given conditions.

        :param table_name: Name of the table from which the record will be deleted.
        :param columns_definition: Condition column for record deletion.
        :param record_values: Value of the condition column to identify the record to be deleted.
        """
    sql_command = f"DELETE FROM {table_name} WHERE {columns_definition} = '{record_values}'"
    print(f'{sql_command =}"')
    # Executes SQL command
    sp_execute(sql_command)


def update_record(table_name, column_definition, record_value, primary_key_name, primary_key_value):
    """
       Updates a record in the specified table.

       :param table_name: Name of the table where the record will be updated.
       :param column_definition: Column to be updated.
       :param record_value: New value to be assigned to the column.
       :param primary_key_name: Name of the primary key column.
       :param primary_key_value: Value of the primary key to identify the record to be updated.
       """
    sql_command = (
                   f" UPDATE {table_name} SET {column_definition} = {record_value} "
                   f" WHERE {primary_key_name} = '{primary_key_value}' "
                   )

    sp_execute(sql_command)


def select_record(table_name, columns_definition, record_values):
    """
        Selects a record from the specified table based on given conditions.

        :param table_name: Name of the table from which the record will be selected.
        :param columns_definition: Condition column for record selection.
        :param record_values: Value of the condition column to identify the record to be selected.
        """
    sql_command = f"SELECT * FROM {table_name} WHERE {columns_definition} = '{record_values}'"
    sp_query(sql_command)


def select_all(table_name):
    """
        Selects all records from the specified table.

        :param table_name: Name of the table from which all records will be selected.
        """
    sql_command = f"SELECT * FROM {table_name}"
    sp_query(sql_command)
