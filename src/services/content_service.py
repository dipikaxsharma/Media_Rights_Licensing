"""
I created this module to hold the business logic for Content.

The service layer sits between:
- the command-line UI (main.py)
- the database layer (content_repo)

This lets me:
- validate inputs
- handle "not found" situations
- keep SQL out of the UI
"""

from typing import List, Optional

from src.models.content import Content
from src.persistence import content_repo


def add_content(
    title: str,
    genre: str | None = None,
    content_type: str | None = None,
    release_year: int | None = None,
    notes: str | None = None,
) -> Content:
    """
    I wrote this function so the UI layer can add new Content
    without knowing anything about SQL or the database.

    It:
    - validates that the title is not empty
    - builds a Content object (with a temporary id)
    - calls content_repo.create_content()
    - returns the saved Content (with real id from SQLite)
    """
    cleaned_title = title.strip()
    if not cleaned_title:
        # I raise ValueError here so the UI can catch it
        # and display a friendly message to the user.
        raise ValueError("Title is required for content.")

    new_content = Content(
        id=0,  # temporary; real id will come from the database
        title=cleaned_title,
        genre=genre.strip() if genre else None,
        content_type=content_type.strip() if content_type else None,
        release_year=release_year,
        notes=notes.strip() if notes else None,
    )

    saved_content = content_repo.create_content(new_content)
    return saved_content


def get_content(content_id: int) -> Optional[Content]:
    """
    I wrote this function so the UI can ask for a single Content
    by id without touching the repository directly.

    It just forwards the call to content_repo.get_content_by_id(),
    but keeping this layer makes it easier to add extra rules later.
    """
    if content_id <= 0:
        # I use this simple check so the UI doesn't try to
        # look up obviously invalid ids like 0 or negative numbers.
        return None

    return content_repo.get_content_by_id(content_id)


def list_contents() -> List[Content]:
    """
    I wrote this function so the menu code can list all content
    without needing to know anything about SQL or the repo.

    Right now it just forwards the call, but I can add
    sorting, filtering, or formatting logic here later.
    """
    return content_repo.list_all_content()
