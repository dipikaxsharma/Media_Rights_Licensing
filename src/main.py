from src.persistence.db import init_db
from src.services import content_service, distributor_service, license_service


def main_menu() -> None:
    """
    I wrote this main menu so the user can choose whether
    to work with content, distributors, or licenses.

    For now it just shows a simple prompt and exits; I will
    fill in the real loops and submenus next.
    """
    print("==== Media Rights Licensing ====")
    print("1. Manage content")
    print("2. Manage distributors")
    print("3. Manage licenses")
    print("Q. Quit")

    choice = input("Choose an option: ").strip().lower()
    if choice == "q":
        print("Goodbye!")
        return

    # For now I just echo the choice; I will hook this up
    # to real submenu functions in the next step.
    print(f"You chose option: {choice}")
    print("Submenus coming next...")


def main() -> None:
    """
    I wrote this main() function as the entry point for the app.

    It:
    - initializes the database (creates tables if needed)
    - then starts the main_menu loop
    """
    init_db()
    main_menu()


if __name__ == "__main__":
    main()
