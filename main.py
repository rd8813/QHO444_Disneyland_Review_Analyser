"""Main program file.
Disneyland Review Analyser.
"""

import process
import tui
import visual


def handle_view_data_menu():
    tui.display_view_data_menu()
    view_choice = input("Enter choice: ").upper()

    if view_choice == "A":
        print("You selected: Display reviews by park")
    elif view_choice == "B":
        print("You selected: Display number of reviews by park and location")
    elif view_choice == "C":
        print("You selected: Display average score by park and year")
    elif view_choice == "X":
        print("Returning to main menu")
    else:
        tui.display_invalid_choice()


def main():
    tui.display_title()
    data = process.load_data("data/disneyland_reviews.csv")
    tui.display_data_loaded(len(data))

    keep_running = True

    while keep_running:
        choice = tui.get_main_menu_choice()

        if choice == "A":
            handle_view_data_menu()
        elif choice == "B":
            tui.display_visualise_data_menu()
        elif choice == "X":
            tui.display_exit_message()
            keep_running = False
        else:
            tui.display_invalid_choice()


if __name__ == "__main__":
    main()