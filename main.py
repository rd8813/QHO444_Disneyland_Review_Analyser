"""Main program file.
Disneyland Review Analyser.
"""

import process
import tui
import visual


def choose_park():
    print("\nChoose a park:")
    print("1 - Disneyland_HongKong")
    print("2 - Disneyland_Paris")
    print("3 - Disneyland_California")

    park_choice = input("Enter choice: ")

    if park_choice == "1":
        return "Disneyland_HongKong"
    elif park_choice == "2":
        return "Disneyland_Paris"
    elif park_choice == "3":
        return "Disneyland_California"
    else:
        print("Invalid park choice")
        return None


def choose_location(data):
    locations = sorted(set(row["Reviewer_Location"] for row in data))

    print("\nAvailable Reviewer Locations:")
    print("-" * 30)

    for i, location in enumerate(locations, start=1):
        print(f"{i}. {location}")

    try:
        location_choice = int(input("\nSelect a location number: "))

        if location_choice < 1 or location_choice > len(locations):
            print("Invalid location choice")
            return None

        return locations[location_choice - 1]

    except ValueError:
        print("Please enter a valid number.")
        return None


def handle_view_data_menu(data):
    tui.display_view_data_menu()
    view_choice = input("Enter choice: ").upper()

    if view_choice == "A":
        park = choose_park()

        if park is None:
            return

        reviews = process.get_reviews_by_park(data, park)

        print(f"\nFound {len(reviews)} reviews")

        for review in reviews[:5]:
            print(review)

    elif view_choice == "B":
        location = choose_location(data)

        if location is None:
            return

        count = 0

        for row in data:
            if row["Reviewer_Location"] == location:
                count += 1

        print(f"\nThere are {count} reviews from {location}.")

    elif view_choice == "C":
        park = choose_park()

        if park is None:
            return

        year = input("Enter year: ")
        average = process.get_average_rating_by_park_and_year(data, park, year)

        if average == 0:
            print("No reviews found for that park and year.")
        else:
            print(f"The average rating for {park} in {year} is {average:.2f}")

    elif view_choice == "D":
        results = process.get_average_score_by_park_and_location(data)

        for park, locations in results.items():
            print(f"\n{park}")
            print("-" * len(park))

            for location, average in locations.items():
                print(f"{location}: {average:.2f}")

    elif view_choice == "X":
        print("Returning to main menu")

    else:
        tui.display_invalid_choice()


def handle_visualise_data_menu(data):
    tui.display_visualise_data_menu()
    visual_choice = input("Enter choice: ").upper()

    if visual_choice == "A":
        visual.show_reviews_by_park_chart(data)

    elif visual_choice == "B":
        park = choose_park()

        if park is None:
            return

        results = process.get_top_locations_by_rating(data, park)

        locations = []
        ratings = []

        for location, rating in results:
            locations.append(location)
            ratings.append(rating)

        visual.show_top_locations_chart(locations, ratings, park)

    elif visual_choice == "C":
        park = choose_park()

        if park is None:
            return

        ratings = process.get_monthly_average_ratings(data, park)

        months = [
            "Jan", "Feb", "Mar", "Apr",
            "May", "Jun", "Jul", "Aug",
            "Sep", "Oct", "Nov", "Dec"
        ]

        visual.show_monthly_ratings_chart(months, ratings, park)

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
            handle_visualise_data_menu(data)

        elif choice == "X":
            tui.display_exit_message()
            keep_running = False

        else:
            tui.display_invalid_choice()


if __name__ == "__main__":
    main()