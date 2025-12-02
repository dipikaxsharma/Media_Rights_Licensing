"""
I created this module to hold all of the database operations
for the Content table.

By keeping SQL here, I keep my service layer and UI code cleaner.
"""

from typing import Optional, List

from src.models.content import Content
from src.persistence.db import get_connection


def create_content(content: Content) -> Content:
    """
    I wrote this function so I can insert a new Content object
    into the SQLite database.

    It:
    - opens a database connection
    - runs an INSERT statement
    - gets the new row id from SQLite
    - returns a fresh Content object with the id filled in
    """
    insert_sql = """
        INSERT INTO content (title, genre, content_type, release_year, notes)
        VALUES (?, ?, ?, ?, ?)
    """

    with get_connection() as conn:
        cursor = conn.execute(
            insert_sql,
            (
                content.title,
                content.genre,
                content.content_type,
                content.release_year,
                content.notes,
            ),
        )
        new_id = cursor.lastrowid
        conn.commit()

    # I return a new Content instance with the generated id
    return Content(
        id=new_id,
        title=content.title,
        genre=content.genre,
        content_type=content.content_type,
        release_year=content.release_year,
        notes=content.notes,
    )
def get_content_by_id(content_id: int) -> Optional[Content]:
    """
    I wrote this function so I can look up a single Content record
    from the database using its primary key id.

    It:
    - opens a database connection
    - runs a SELECT statement with the id as a parameter
    - if a row is found, converts it into a Content object
    - if nothing is found, returns None
    """
    select_sql = """
        SELECT id, title, genre, content_type, release_year, notes
        FROM content
        WHERE id = ?
    """

    with get_connection() as conn:
        cursor = conn.execute(select_sql, (content_id,))
        row = cursor.fetchone()

    if row is None:
        # I return None if there is no matching row so the caller can
        # handle "not found" cases in the service or UI layer.
        return None

    # I build and return a Content object from the row.
    return Content(
        id=row["id"],
        title=row["title"],
        genre=row["genre"],
        content_type=row["content_type"],
        release_year=row["release_year"],
        notes=row["notes"],
    )

def list_all_content() -> List[Content]:
    """
    I wrote this function so I can pull every content record
    from the database and convert each row into a Content object.

    It:
    - opens the database
    - runs a SELECT query for all rows
    - loops through the rows
    - turns each into a Content object
    - returns the list
    """
    select_sql = """
        SELECT id, title, genre, content_type, release_year, notes
        FROM content
        ORDER BY id
    """

    with get_connection() as conn:
        cursor = conn.execute(select_sql)
        rows = cursor.fetchall()

    contents: List[Content] = []
    for row in rows:
        contents.append(
            Content(
                id=row["id"],
                title=row["title"],
                genre=row["genre"],
                content_type=row["content_type"],
                release_year=row["release_year"],
                notes=row["notes"],
            )
        )

    return contents
def update_content(content: Content) -> bool:
    """
    I wrote this function so I can update an existing Content
    record in the database.

    It:
    - runs an UPDATE statement using the content.id as the key
    - returns True if a row was actually updated
    - returns False if no rows were changed (for example, bad id)
    """
    update_sql = """
        UPDATE content
        SET title = ?,
            genre = ?,
            content_type = ?,
            release_year = ?,
            notes = ?
        WHERE id = ?
    """

    with get_connection() as conn:
        cursor = conn.execute(
            update_sql,
            (
                content.title,
                content.genre,
                content.content_type,
                content.release_year,
                content.notes,
                content.id,
            ),
        )
        conn.commit()

    # rowcount tells me how many rows were affected by the UPDATE
    return cursor.rowcount > 0
