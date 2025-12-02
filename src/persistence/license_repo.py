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
