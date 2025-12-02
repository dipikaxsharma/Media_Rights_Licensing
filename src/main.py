from src.persistence.db import init_db
from src.services import content_service, distributor_service, license_service


def _prompt_int(prompt: str) -> int | None:
    """
    I wrote this helper so I can safely ask the user for an integer id.
    If the user types something that is not a number, I return None
    instead of crashing the program.
    """
    raw = input(prompt).strip()
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError:
        print("Please enter a whole number.")
        return None


def content_menu() -> None:
    """
    I wrote this content submenu so the user can manage Content records:
    - list all content
    - add new content
    - view one content by id
    - delete content by id
    """
    while True:
        print("\n==== Content Menu ====")
        print("1. List all content")
        print("2. Add new content")
        print("3. View content by id")
        print("4. Delete content by id")
        print("B. Back to main menu")

        choice = input("Choose an option: ").strip().lower()

        # ---- LIST ----
        if choice == "1":
            contents = content_service.list_contents()
            if not contents:
                print("No content found.")
            else:
                print("\n-- All Content --")
                for c in contents:
                    print(c)

        # ---- ADD ----
        elif choice == "2":
            print("\n-- Add New Content --")
            title = input("Title (required): ")
            genre = input("Genre (optional): ")
            content_type = input("Content type (optional, e.g., Movie, Series): ")
            year_raw = input("Release year (optional, number): ").strip()
            notes = input("Notes (optional): ")

            release_year = None
            if year_raw:
                try:
                    release_year = int(year_raw)
                except ValueError:
                    print("Invalid year, leaving it blank.")
                    release_year = None

            try:
                new_content = content_service.add_content(
                    title=title,
                    genre=genre or None,
                    content_type=content_type or None,
                    release_year=release_year,
                    notes=notes or None,
                )
                print(f"Created content with id {new_content.id}.")
            except ValueError as e:
                print(f"Could not create content: {e}")

        # ---- VIEW ----
        elif choice == "3":
            content_id = _prompt_int("Enter content id: ")
            if content_id is None:
                continue

            content = content_service.get_content(content_id)
            if content is None:
                print(f"No content found with id {content_id}.")
            else:
                print("\n-- Content Details --")
                print(repr(content))

        # ---- DELETE ----
        elif choice == "4":
            content_id = _prompt_int("Enter content id to delete: ")
            if content_id is None:
                continue

            # This will work once delete_content exists in content_service
            if hasattr(content_service, "delete_content"):
                deleted = content_service.delete_content(content_id)
            else:
                deleted = False

            if deleted:
                print(f"Deleted content with id {content_id}.")
            else:
                print(f"No content found with id {content_id}.")

        # ---- BACK ----
        elif choice == "b":
            break

        else:
            print("Invalid choice. Please try again.")


def main_menu() -> None:
    """
    I wrote this main menu so the user can choose whether
    to work with content, distributors, or licenses.

    It runs in a loop until the user chooses to quit.
    """
    while True:
        print("\n==== Media Rights Licensing ====")
        print("1. Manage content")
        print("2. Manage distributors")
        print("3. Manage licenses")
        print("Q. Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        elif choice == "1":
            content_menu()

        elif choice == "2":
            print("Distributor menu coming soon...")

        elif choice == "3":
            print("License menu coming soon...")

        else:
            print("Invalid choice. Please try again.")


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
