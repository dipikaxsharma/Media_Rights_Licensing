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
