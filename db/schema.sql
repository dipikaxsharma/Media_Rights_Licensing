-- ===========================
-- CONTENT TABLE
-- ===========================
CREATE TABLE IF NOT EXISTS content (
    id           INTEGER PRIMARY KEY,
    title        TEXT NOT NULL,
    genre        TEXT,
    content_type TEXT,
    release_year INTEGER,
    notes        TEXT
);

-- ===========================
-- DISTRIBUTOR TABLE
-- ===========================
CREATE TABLE IF NOT EXISTS distributor (
    id            INTEGER PRIMARY KEY,
    name          TEXT NOT NULL,
    contact_email TEXT,
    region        TEXT
);

-- ===========================
-- LICENSE TABLE (XREF)
-- ===========================
CREATE TABLE IF NOT EXISTS license_xref (
    id             INTEGER PRIMARY KEY,
    content_id     INTEGER NOT NULL,
    distributor_id INTEGER NOT NULL,
    start_date     TEXT,
    end_date       TEXT,
    terms          TEXT,
    FOREIGN KEY (content_id) REFERENCES content(id),
    FOREIGN KEY (distributor_id) REFERENCES distributor(id)
);
