🎬 Media Rights Licensing

IT566 – Computer Scripting Techniques | Fall 2025

A console-based, multi-layered Python application that manages licensing relationships between media content and distributors.
Built using SQLite and Bash automation, following modular design and data-driven principles.

⚙️ Features

Console interface for managing content, distributors, and licenses

Multi-layer architecture separating data, logic, and interface

SQLite3 database with content, distributor, and license_xref tables

Bash scripts for setup, initialization, and testing

Logging & configuration using the IT566 Application Framework

🧩 Tech Stack

Language: Python 3

Database: SQLite3

Automation: Bash

Version Control: Git

📂 Folder Structure
media_rights_licensing/
│
├── src/
│   ├── main.py
│   ├── data/
│   │   ├── database.py
│   │   └── models.py
│   ├── logic/
│   │   └── license_manager.py
│   └── interface/
│       └── menu.py
│
├── scripts/
│   ├── init_db.sh
│   ├── run_tests.sh
│   └── run_app.sh
│
├── data/
│   └── media_rights.db
│
├── logs/
│   └── app.log
│
├── config/
│   └── settings.json
│
└── README.md

🚀 Setup Instructions

Clone the repository:

git clone https://github.com/yourusername/media_rights_licensing.git
cd media_rights_licensing


Initialize the database:

bash scripts/init_db.sh


Run the application:

python src/main.py


🧠 Learning Goals

Develop modular, data-driven applications

Automate workflows using Bash

Implement structured programming and database logic

Practice professional Git version control habits
