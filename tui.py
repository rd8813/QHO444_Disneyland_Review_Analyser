def display_title():
    title = "Disneyland Review Analyser"
    print("-" * len(title))
    print(title)
    print("-" * len(title))


def display_data_loaded(number_of_rows):
    print("Dataset loaded successfully")
    print(f"There are {number_of_rows} rows in the dataset.")


def get_main_menu_choice():
    print("\nPlease enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")

    choice = input("Enter choice: ")
    return choice.upper()


def display_view_data_menu():
    print("\nView Data Menu")
    print("[A] Display reviews by park")
    print("[B] Display number of reviews by park and location")
    print("[C] Display average score by park and year")
    print("[X] Return to Main Menu")


def display_visualise_data_menu():
    print("\nPlease enter one of the following options:")
    print("[A] Most reviewed Parks")
    print("[B] Park Ranking by Nationality")
    print("[C] Most Popular Month by Park")


def display_invalid_choice():
    print("Invalid choice. Please try again.")


def display_exit_message():
    print("Thank you. Program closed")