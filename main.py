"""Main program file.
Disneyland Review Analyser.
"""

import process
import tui
import visual


def handle_view_data_menu(data):
    tui.display_view_data_menu()
    view_choice = input("Enter choice: ").upper()

    if view_choice == "A":

        print("\nChoose a park:")
        print("1 - Disneyland_HongKong")
        print("2 - Disneyland_Paris")
        print("3 - Disneyland_California")

        park_choice = input("Enter choice: ")

        if park_choice == "1":
            park = "Disneyland_HongKong"
        elif park_choice == "2":
            park = "Disneyland_Paris"
        elif park_choice == "3":
            park = "Disneyland_California"
        else:
            print("Invalid park choice")
            return

        reviews = process.get_reviews_by_park(data, park)

        print(f"\nFound {len(reviews)} reviews")

        for review in reviews[:5]:
            print(review)


    elif view_choice == "B":

        location = input("Enter reviewer location: ")

        count = 0

        for row in data:

            if row["Reviewer_Location"].lower() == location.lower():
                count += 1

        print(f"There are {count} reviews from {location}.")

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
            handle_view_data_menu(data)
        elif choice == "B":
            tui.display_visualise_data_menu()
        elif choice == "X":
            tui.display_exit_message()
            keep_running = False
        else:
            tui.display_invalid_choice()


if __name__ == "__main__":
    main()