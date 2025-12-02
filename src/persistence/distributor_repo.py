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
def list_all_distributors() -> List[Distributor]:
    """
    I wrote this function so I can pull every distributor record
    from the database and convert each row into a Distributor object.

    It:
    - opens the database
    - runs a SELECT query for all rows
    - loops through the rows
    - turns each into a Distributor object
    - returns the list
    """
    select_sql = """
        SELECT id, name, contact_email, region
        FROM distributor
        ORDER BY id
    """

    with get_connection() as conn:
        cursor = conn.execute(select_sql)
        rows = cursor.fetchall()

    distributors: List[Distributor] = []
    for row in rows:
        distributors.append(
            Distributor(
                id=row["id"],
                name=row["name"],
                contact_email=row["contact_email"],
                region=row["region"],
            )
        )

    return distributors
def update_distributor(distributor: Distributor) -> bool:
    """
    I wrote this function so I can update an existing Distributor
    record in the database.

    It:
    - runs an UPDATE statement using distributor.id as the key
    - returns True if a row was actually updated
    - returns False if no rows were changed (for example, bad id)
    """
    update_sql = """
        UPDATE distributor
        SET name = ?,
            contact_email = ?,
            region = ?
        WHERE id = ?
    """

    with get_connection() as conn:
        cursor = conn.execute(
            update_sql,
            (
                distributor.name,
                distributor.contact_email,
                distributor.region,
                distributor.id,
            ),
        )
        conn.commit()

    # rowcount tells me how many rows were affected by the UPDATE
    return cursor.rowcount > 0
def delete_distributor(distributor_id: int) -> bool:
    """
    I wrote this function so I can delete a Distributor record
    from the database by its id.

    It:
    - runs a DELETE statement using the id
    - returns True if a row was actually deleted
    - returns False if no row matched that id
    """
    delete_sql = """
        DELETE FROM distributor
        WHERE id = ?
    """

    with get_connection() as conn:
        cursor = conn.execute(delete_sql, (distributor_id,))
        conn.commit()

    # If rowcount is 0, nothing was deleted (bad or missing id)
    return cursor.rowcount > 0
