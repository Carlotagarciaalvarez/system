def show_menu():
    """
    Function to display the menu option
    """
    print("============================")
    print("===      M E N U         ===")
    print("===----------------------===")
    print("=== 1)  Create Table     ===")
    print("=== 2)  Drop Table       ===")
    print("=== 3)  Insert record    ===")
    print("=== 4)  Update record    ===")
    print("=== 5)  Delete record    ===")
    print("=== 6)  Find record      ===")
    print("=== 7)  Export records   ===")
    print("=== 8)  Plot Graphic     ===")
    print("=== 9)  Import CSV       ===")
    print("=== 10) Show all records ===")
    print("=== 11) Plot ADA Graphic ===")
    print("=== 0)  EXIT             ===")
    print("============================")


def select_option():
    """
       Function to prompt the user to select an option from the menu.
       Entry point of the options
       :return: The selected option.
       """
    try:
        # Convert user input to an integer
        sel_option = int(input('Select your option: '))
    except ValueError:
        #  If input cannot be converted to an integer, notify the user
        print('Invalid option, please try again.')
    else:
        # Return the selected option if input is valid
        return sel_option
