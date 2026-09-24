# My Year in Color

A terminal-based mood and journaling application written in Python. **My Year in Color** allows users to record daily entries, associate them with an emotion represented by a colour, and store their entries in a SQLite database.

The project was originally built using JSON storage and was later developed further as part of **LifeSuite**, introducing a SQLite database and separate database-query layer.

## Features

- 📝 Create journal entries with a date, mood and notes
- 🎨 Associate emotions with different colours
- 🗄️ Store entries using SQLite
- 👀 View previously recorded entries
- ✏️ Edit existing journal entries
- 🗑️ Delete entries
- 💻 Interact with the application through a terminal menu

## Technologies

- **Python**
- **SQLite**
- `sqlite3`
- `datetime`
- Terminal-based interface

## Project Structure

```text
.
├── myic.py
└── databaseQuery.py
```

### `myic.py`

Contains the main application logic and user interaction.

This includes functionality for:

- Adding entries
- Viewing entries
- Editing entries
- Deleting entries
- Selecting emotions/colours

### `databaseQuery.py`

Contains the SQLite database functionality.

The module handles:

- Connecting to the database
- Adding entries
- Retrieving entries
- Retrieving individual entries
- Editing entries
- Deleting entries

Keeping the database operations separate from the application logic was intended to make the project easier to develop and maintain.

## Mood System

Entries are associated with a colour representing a particular mood.

The current default categories are:

| Colour | Emotion |
|---|---|
| 🟣 Purple | Happy |
| 🔴 Red | Stressed / Annoyed |
| ⚪ Grey | Average |
| 🟢 Green | Productive |
| 🔵 Blue | Content / At Peace |
| ⚫ Black | Idk Idc|

The colour-to-emotion system can be extended with additional categories.

## Database

The application uses SQLite to store journal entries.

Each entry contains information including:

```text
entryID
date
emotion
notes
time
```

The database operations are separated into `databaseQuery.py`, where SQL queries are used to insert, retrieve, update and delete entries.

## Getting Started

### Requirements

- Python 3
- SQLite3

Python's `sqlite3` module is included with standard Python installations, so no external database package is required.

### Clone the repository

```bash
git clone https://github.com/KazurK/My-Year-in-Color.git
cd My-Year-in-Color
```

### Configure the database

Before running the application, update the database path in `databaseQuery.py`:

```python
dbPath = "/path/to/your/lifesuite.db"
```

The database must contain an `entry` table with the columns required by the application.

### Run the application

```bash
python myic.py
```

The application will present a terminal menu allowing you to select the available functions.

## Development

My Year in Color started as a small Python project designed to experiment with storing and displaying personal mood data.

The project has since been used to explore:

- Python functions and program structure
- File-based data storage
- SQLite databases
- SQL queries
- CRUD operations
- Separating application logic from database logic
- Terminal-based user interfaces

The project is still under development, with further improvements planned.

## Future Improvements

Potential improvements include:

- 📅 A proper calendar interface for viewing entries
- 🎨 Visual colour representation of moods
- 📊 Mood statistics and trends
- 🔍 Searching and filtering entries
- ⏱️ Improved date and time handling
- ⚙️ Improved database configuration
- 🖥️ A graphical user interface
- 🔐 Better handling of user data

## Project Status

**In development**

This project is primarily a learning project and is being developed incrementally as I learn more about Python, databases and software development.

## Author

**Jaden**

Computer Science student interested in software engineering, systems and application development.
