# Engineering Notebook – Media Rights Licensing Project
---
## ~5 hours
**Work Completed:**
- Set up full project folder structure (src, db, tests, models, services, persistence)
- Created all empty Python modules required by the IT566 application framework
- Added `schema.sql` and wrote initial SQLite database schema
- Created `main.py` starter entry point
- Created `build.sh` starter automation script
- Studied Chapters 1–25 to understand requirements and mapped out project blueprint
**Notes / Reflection:**
- Ensured database schema follows project guidelines (primary/foreign keys)
- Verified files are correctly placed for multi-layer architecture

- I added the to_dict and from_dict methods to the Distributor class today. 
  I wrote them so the Distributor objects can be saved to the SQLite database 
  and reconstructed later. This will make persistence and testing much easier.

- I wrote the create_content function in content_repo.py so I can insert Content objects into the SQLite DB and get back the new id

- I added list_all_content to content_repo so I can pull all content records from the database and convert them into Content objects for the menu to display.

