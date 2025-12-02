"""
I created this module to hold the business logic for Distributor.

The service layer sits between:
- the command-line UI (main.py)
- the database layer (distributor_repo)

This lets me:
- validate inputs
- handle "not found" situations
- keep SQL out of the UI
"""

from typing import List, Optional

from src.models.distributor import Distributor
from src.persistence import distributor_repo


def add_distributor(
    name: str,
    contact_email: str | None = None,
    region: str | None = None,
) -> Distributor:
    """
    I wrote this function so the UI can add new distributors
    without talking to the repository or SQL directly.

    It:
    - validates that the name is not empty
    - does a simple check on the email (if provided)
    - builds a Distributor object (with a temporary id)
    - calls distributor_repo.create_distributor()
    - returns the saved Distributor (with real id from SQLite)
    """
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("Distributor name is required.")

    cleaned_email = contact_email.strip() if contact_email else None
    if cleaned_email and "@" not in cleaned_email:
        # Simple validation so obviously bad emails can be caught
        raise ValueError("Contact email must contain '@' if provided.")

    cleaned_region = region.strip() if region else None

    new_distributor = Distributor(
        id=0,  # temporary; real id will come from the database
        name=cleaned_name,
        contact_email=cleaned_email,
        region=cleaned_region,
    )

    saved_distributor = distributor_repo.create_distributor(new_distributor)
    return saved_distributor


def get_distributor(distributor_id: int) -> Optional[Distributor]:
    """
    I wrote this function so the UI can ask for a single Distributor
    by id without talking to the repository directly.

    It also blocks obviously invalid ids like 0 or negatives.
    """
    if distributor_id <= 0:
        return None

    return distributor_repo.get_distributor_by_id(distributor_id)


def list_distributors() -> List[Distributor]:
    """
    I wrote this function so the menu code can list all distributors
    without needing to know anything about SQL or the repository.

    Right now it just forwards the call, but I could add sorting
    or filtering logic here later.
    """
    return distributor_repo.list_all_distributors()
