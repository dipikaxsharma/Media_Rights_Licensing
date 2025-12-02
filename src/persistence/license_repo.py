"""
I created this module to hold all of the database operations
for the LicenseXref table. Each row represents one license
between a content item and a distributor.
"""

from typing import Optional, List

from src.models.license_xref import LicenseXref
from src.persistence.db import get_connection


def create_license(license_xref: LicenseXref) -> LicenseXref:
    """
    I wrote this function so I can insert a new LicenseXref object
    into the SQLite database.

    It:
    - opens a database connection
    - runs an INSERT statement
    - gets the new row id from SQLite
    - returns a fresh LicenseXref object with the id filled in
    """
    insert_sql = """
        INSERT INTO license_xref (
            content_id,
            distributor_id,
            start_date,
            end_date,
            terms
        )
        VALUES (?, ?, ?, ?, ?)
    """

    with get_connection() as conn:
        cursor = conn.execute(
            insert_sql,
            (
                license_xref.content_id,
                license_xref.distributor_id,
                license_xref.start_date,
                license_xref.end_date,
                license_xref.terms,
            ),
        )
        new_id = cursor.lastrowid
        conn.commit()

    return LicenseXref(
        id=new_id,
        content_id=license_xref.content_id,
        distributor_id=license_xref.distributor_id,
        start_date=license_xref.start_date,
        end_date=license_xref.end_date,
        terms=license_xref.terms,
    )
def get_license_by_id(license_id: int) -> Optional[LicenseXref]:
    """
    I wrote this function so I can look up a single LicenseXref
    record in the database using its primary key id.

    It:
    - opens a database connection
    - runs a SELECT with the id as a parameter
    - if a row is found, converts it into a LicenseXref object
    - if nothing is found, returns None
    """
    select_sql = """
        SELECT id, content_id, distributor_id, start_date, end_date, terms
        FROM license_xref
        WHERE id = ?
    """

    with get_connection() as conn:
        cursor = conn.execute(select_sql, (license_id,))
        row = cursor.fetchone()

    if row is None:
        # I return None if there is no matching row so the caller can
        # handle "not found" cases in the service or UI layer.
        return None

    return LicenseXref(
        id=row["id"],
        content_id=row["content_id"],
        distributor_id=row["distributor_id"],
        start_date=row["start_date"],
        end_date=row["end_date"],
        terms=row["terms"],
    )
def list_all_licenses() -> List[LicenseXref]:
    """
    I wrote this function so I can pull every license record
    from the database and convert each row into a LicenseXref object.

    It:
    - opens the database
    - runs a SELECT query for all rows
    - loops through the rows
    - turns each into a LicenseXref object
    - returns the list
    """
    select_sql = """
        SELECT id, content_id, distributor_id, start_date, end_date, terms
        FROM license_xref
        ORDER BY id
    """

    with get_connection() as conn:
        cursor = conn.execute(select_sql)
        rows = cursor.fetchall()

    licenses: List[LicenseXref] = []
    for row in rows:
        licenses.append(
            LicenseXref(
                id=row["id"],
                content_id=row["content_id"],
                distributor_id=row["distributor_id"],
                start_date=row["start_date"],
                end_date=row["end_date"],
                terms=row["terms"],
            )
        )

    return licenses
def update_license(license_xref: LicenseXref) -> bool:
    """
    I wrote this function so I can update an existing LicenseXref
    record in the database.

    It:
    - runs an UPDATE statement using license_xref.id as the key
    - returns True if a row was actually updated
    - returns False if no rows were changed (for example, bad id)
    """
    update_sql = """
        UPDATE license_xref
        SET content_id = ?,
            distributor_id = ?,
            start_date = ?,
            end_date = ?,
            terms = ?
        WHERE id = ?
    """

    with get_connection() as conn:
        cursor = conn.execute(
            update_sql,
            (
                license_xref.content_id,
                license_xref.distributor_id,
                license_xref.start_date,
                license_xref.end_date,
                license_xref.terms,
                license_xref.id,
            ),
        )
        conn.commit()

    # rowcount tells me how many rows were affected by the UPDATE
    return cursor.rowcount > 0
