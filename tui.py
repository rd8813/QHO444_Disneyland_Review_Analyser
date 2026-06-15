def display_title():
    title = "Disneyland Review Analyser"
    print ("-" * len(title))
    print (title)
    print ("-" * len(title))

def display_data_loaded (number_of_rows):
    print ("Dataset loaded successfully")
    print (f"There are {number_of_rows} row in the dataset.")

def get_main_menu_choice():
    print ("\n Please enter the letter which corresponds with your desired menu choice:")
    print ("[A] View Data")
    print ("[B] Visualise Data")
    print ("[X] Exit")
    choice = input ("Enter choice: ")
    return choice.upper()

def display_view_data_menu():
    print ("You have chosen option A-View Data")

def display_visualise_data_menu():
    print ("You have chosen option B-Visualise Data")

def display_invalid_choice():
    print ("Invalid choice. Please try again.")

def display_exit_message():
    print ("Thank you. Program closed")
