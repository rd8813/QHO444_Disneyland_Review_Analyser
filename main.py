"""main program file
Disneyland Review Analyser"""

import process
import tui
import visual


def main():
    tui.display_title()
    data = process.load_data("data/disneyland_reviews.csv")
    tui.display_data_loaded(len(data))

    keep_running = True
    while keep_running:
        choice=tui.get_main_menu_choice()

        if choice=="A":
            tui.display_view_data_menu()
        elif choice=="B":
            tui.display_visualise_data_menu()
        elif choice=="X":
            tui.display_exit_message()
            keep_running=False
        else:
            tui.display_invalid_choice()
if __name__ == "__main__":
    main()


