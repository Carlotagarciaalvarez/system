# Importing necessary functions from various modules
from menu_xy import (show_menu,
                     select_option,
                     )
from business import (business_create_table,
                      set_business_record_values,
                      set_update_record,
                      set_delete_record,
                      get_select_record,
                      business_drop_table,
                      get_select_all
                      )
from export_csv import export_data
from import_csv import read_business_csv
from graphics import plot_graphic
from ada import plot_graphic as ada_plot


def main():
    """
    Main routine entry point of the system.
    By: Carlota Garcia
    Date: 04/02/2024
    :return: Menu operation
    """
    # Display the menu
    show_menu()
    # Initialize the count for number of selections
    number_of_selections = 0
    while True:
        # Prompt user tu select an option from the menu
        selected_option = select_option()
        # Print the selected option for debugging
        print(f' The option is: {selected_option =}')
        # Increment the count of selections
        number_of_selections += 1
        # If user has made more than 3 selections, show the menu again
        if number_of_selections > 3:
            show_menu()
            number_of_selections = 0

        # If user selects option is 0, finish the running process
        if selected_option == 0:
            print('Good bye!')
            break
        else:
            run_selected_option(selected_option)


def run_selected_option(selected_option):
    try:
        # Execute the appropriate function based on the selected option
        if int(selected_option) == 1:
            business_create_table()

        if int(selected_option) == 2:
            business_drop_table()

        if int(selected_option) == 3:
            set_business_record_values()

        if int(selected_option) == 4:
            set_update_record()

        if int(selected_option) == 5:
            set_delete_record()

        if int(selected_option) == 6:
            get_select_record()

        if int(selected_option) == 7:
            export_data()

        if int(selected_option) == 8:
            plot_graphic()

        if int(selected_option) == 9:
            read_business_csv()

        if int(selected_option) == 10:
            get_select_all()

        if int(selected_option) == 11:
            ada_plot()

    except:
        # Handle errors that might occur during execution
        print('Error:')


if __name__ == '__main__':
    # Start the main program
    main()
