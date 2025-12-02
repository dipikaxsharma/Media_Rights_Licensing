"""
I created this module to centralize all of my database setup and
connection logic for the Media Rights Licensing project.

The idea is:
- get_connection() gives me a SQLite connection to use in other files
- init_db() runs my schema.sql so my tables are created if needed

This keeps database details in one place instead of scattering them
around the app.
"""

import sqlite3
from pathlib import Path


# I am using a relative path here so that as long as I run the app
# from the project root, the database file will live in ./db/media.db
BASE_DIR = Path(__file__).resolve().parents[2]   # persistence -> src -> project root
DB_PATH = BASE_DIR / "db" / "media.db"
SCHEMA_PATH = BASE_DIR / "db" / "schema.sql"


def get_connection() -> sqlite3.Connection:
    """
    I use this function anywhere I need to talk to the database.

    It opens a connection to the SQLite database file and turns on
    row_factory so I can access columns by name (like row["title"])
    instead of only by index.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """
    I call this at the start of the program (or from a one-time script)
    to make sure my tables exist.

    What it does:
    - opens schema.sql
    - reads the full SQL script
    - executes it against the SQLite connection

    This matches the "project database guidelines" from the rubric.
    """
    with get_connection() as conn:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            schema_sql = f.read()
        conn.executescript(schema_sql)
        conn.commit()
