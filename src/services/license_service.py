"""
I created this module to hold the business logic for LicenseXref.

The service layer sits between:
- the command-line UI (main.py)
- the database layer (license_repo, content_repo, distributor_repo)

This lets me:
- validate that content and distributor ids are real
- keep SQL out of the UI
- keep the license rules in one place
"""

from typing import List, Optional

from src.models.license_xref import LicenseXref
from src.persistence import license_repo, content_repo, distributor_repo
def add_license(
    content_id: int,
    distributor_id: int,
    start_date: str | None = None,
    end_date: str | None = None,
    terms: str | None = None,
) -> LicenseXref:
    """
    I wrote this function so the UI can create a new license
    between an existing content item and an existing distributor.

    It:
    - checks that the ids are positive
    - verifies that the content exists
    - verifies that the distributor exists
    - builds a LicenseXref object (with a temporary id)
    - calls license_repo.create_license()
    - returns the saved LicenseXref (with real id from SQLite)
    """
    if content_id <= 0 or distributor_id <= 0:
        raise ValueError("Content id and distributor id must be positive integers.")

    # I make sure the content exists before creating the license
    content = content_repo.get_content_by_id(content_id)
    if content is None:
        raise ValueError(f"No content found with id {content_id}.")

    # I make sure the distributor exists before creating the license
    distributor = distributor_repo.get_distributor_by_id(distributor_id)
    if distributor is None:
        raise ValueError(f"No distributor found with id {distributor_id}.")

    new_license = LicenseXref(
        id=0,  # temporary; real id will come from the database
        content_id=content_id,
        distributor_id=distributor_id,
        start_date=start_date,
        end_date=end_date,
        terms=terms.strip() if terms else None,
    )

    saved_license = license_repo.create_license(new_license)
    return saved_license
def get_license(license_id: int) -> Optional[LicenseXref]:
    """
    I wrote this function so the UI can ask for a single license
    by id without talking to the repository directly.

    It also guards against obviously invalid ids.
    """
    if license_id <= 0:
        return None

    return license_repo.get_license_by_id(license_id)


def list_licenses() -> List[LicenseXref]:
    """
    I wrote this function so the menu code can list all licenses
    without knowing anything about the database layer.

    Right now it just forwards the call, but I could later add:
    - filtering by content
    - filtering by distributor
    - filtering by active date range
    """
    return license_repo.list_all_licenses()
def update_license(license_xref: LicenseXref) -> bool:
    """
    I wrote this function so I can update an existing license record.

    For now it just forwards the call to license_repo.update_license(),
    but I could later add more validation here (for example, checking
    that content and distributor ids still exist).
    """
    return license_repo.update_license(license_xref)


def delete_license(license_id: int) -> bool:
    """
    I wrote this function so the UI can delete a license by id.

    It returns True if a row was deleted and False if no matching id
    was found in the database.
    """
    if license_id <= 0:
        return False

    return license_repo.delete_license(license_id)
