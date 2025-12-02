"""
I created this module to hold all of the database operations
for the Distributor table.
"""

from typing import Optional, List

from src.models.distributor import Distributor
from src.persistence.db import get_connection


def create_distributor(distributor: Distributor) -> Distributor:
    """
    I wrote this function so I can insert a new Distributor object
    into the SQLite database.

    It:
    - opens a database connection
    - runs an INSERT statement
    - gets the new row id from SQLite
    - returns a fresh Distributor object with the id filled in
    """
    insert_sql = """
        INSERT INTO distributor (name, contact_email, region)
        VALUES (?, ?, ?)
    """

    with get_connection() as conn:
        cursor = conn.execute(
            insert_sql,
            (
                distributor.name,
                distributor.contact_email,
                distributor.region,
            ),
        )
        new_id = cursor.lastrowid
        conn.commit()

    return Distributor(
        id=new_id,
        name=distributor.name,
        contact_email=distributor.contact_email,
        region=distributor.region,
    )
def get_distributor_by_id(distributor_id: int) -> Optional[Distributor]:
    """
    I wrote this function so I can look up a single Distributor
    record in the database using its primary key id.

    It:
    - opens a database connection
    - runs a SELECT with the id as a parameter
    - if a row is found, converts it into a Distributor object
    - if nothing is found, returns None
    """
    select_sql = """
        SELECT id, name, contact_email, region
        FROM distributor
        WHERE id = ?
    """

    with get_connection() as conn:
        cursor = conn.execute(select_sql, (distributor_id,))
        row = cursor.fetchone()

    if row is None:
        # I return None if there is no matching row so the caller can
        # handle "not found" cases in the service or UI layer.
        return None

    return Distributor(
        id=row["id"],
        name=row["name"],
        contact_email=row["contact_email"],
        region=row["region"],
    )
