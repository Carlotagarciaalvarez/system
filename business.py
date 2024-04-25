# Importing necessary functions from database
from database import (create_table,
                      drop_table,
                      insert_record,
                      delete_record,
                      select_record,
                      update_record,
                      select_all
                      )


def business_create_table():
    # Creates a 'business' table in the database with specified columns.
    my_table_name = 'business'
    my_columns = ''' 
            id int, 
            x float,
            y float,
            z float
    '''
    create_table(my_table_name, my_columns)


def business_drop_table():
    # Drops the 'business' table from the database.
    my_table_name = 'business'
    drop_table(my_table_name)


def business_insert_record(record_values):
    """
    Inserts a record into the 'business' table with given values.

    :param record_values: Values of the record to be inserted.
    """
    my_table_name = 'business'
    columns_definition = ''' 
                id,
                x,
                y,
                z
       '''

    insert_record(my_table_name, columns_definition, record_values)


def set_business_record_values():
    # Sets the values for a new record to be inserted into the 'business' table.
    my_id = input('Insert the Id value: ')
    my_x = input('Insert the X value: ')
    my_y = input('Insert the Y value: ')
    my_z = input('Insert the Z value: ')

    record_values = f" {my_id}, {my_x}, {my_y}, {my_z}"

    business_insert_record(record_values)


def set_delete_record():
    # Deletes a record from the 'business' table based on given Id.
    my_table_name = 'business'
    my_columns_definition = 'id'
    my_id = input('Insert the Id value: ')

    delete_record(my_table_name, my_columns_definition, my_id)


def get_select_record():
    # Selects a record from the 'business' table based on given Id.
    my_table_name = 'business'
    my_columns_definition = 'id'
    my_id = input('Insert the Id value: ')

    select_record(my_table_name, my_columns_definition, my_id)


def set_update_record():
    # Updates a record in the 'business' table based on given Id and column name/value.
    my_table_name = 'business'
    my_primary_key_name = 'id'

    my_id = input('Insert the Id value: ')
    my_column = input('Insert the column name: ')
    my_value = input('Insert the column value: ')

    update_record(my_table_name, my_column, my_value, my_primary_key_name, my_id)


def get_select_all():
    # Selects all records from the 'business' table.
    my_table_name = 'business'
    select_all(my_table_name)
