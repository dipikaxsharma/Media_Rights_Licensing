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
