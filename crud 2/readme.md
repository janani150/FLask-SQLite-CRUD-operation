Flask + SQLite CRUD Application
Project Overview

This project is a simple web application built with Flask and SQLite that allows users to Create, Read, Update, and Delete (CRUD) user records. It demonstrates how to integrate a Python backend with an SQLite database and a Bootstrap-powered frontend.



Features

Add Users:

Input user details like Name, Contact, Address, Email, and Age.

View Users:

Display all users in a table format with serial numbers.

Edit Users:

Update all details of an existing user.

Delete Users:

Remove a user record with confirmation.

Flash Messages:

Shows success or warning messages when a user is added, updated, or deleted.

Responsive Design:

Uses Bootstrap 4 for a clean and responsive UI.

Database

Database: SQLite (db_web.db)

Table: users

Columns:

Column	Type	Description
UID	INTEGER PRIMARY KEY AUTOINCREMENT	Unique ID for each user
UNAME	TEXT	User’s full name
CONTACT	TEXT	Phone number or contact info
address	TEXT	User address
email	TEXT	User email
age	INTEGER	User age

The table is created automatically if it does not exist.

Project Structure
flask_crud_project/
│
├── app.py                # Main Flask application with routes and database connection
├── db_web.db             # SQLite database file
├── templates/            # HTML templates
│   ├── layout.html       # Base layout with Bootstrap and flash messages
│   ├── index.html        # Displays list of all users
│   ├── add_user.html     # Form to add a new user
│   └── edit_user.html    # Form to edit an existing user
└── static/               # Optional: CSS, JS, or image files (if needed)

How It Works

Homepage (/ or /index):

Connects to SQLite database and fetches all users.

Displays them in a table with options to Edit or Delete.

Add User (/add_user):

Opens a form to enter user details.

On submit, inserts the data into the database and shows a success flash message.

Edit User (/edit_user/<uid>):

Opens a form pre-filled with the selected user’s data.

On submit, updates the record in the database and shows a success flash message.

Delete User (/delete_user/<uid>):

Deletes the selected user from the database after confirmation.

Shows a warning flash message.

Flash Messages:

Used to inform the user about actions like adding, updating, or deleting a record.

Database Connection:

Each route connects to db_web.db using sqlite3.

row_factory = sqlite3.Row is used for dictionary-style access in templates (row['UNAME']).

Dependencies

Python 3.x

Flask

SQLite (built into Python)

Bootstrap 4 (via CDN in templates)

You can install Flask using:

pip install flask

How to Run

Clone the repository:

git clone https://github.com/yourusername/flask_crud_project.git


Navigate to the project folder:

cd flask_crud_project


Run the Flask app:

python app.py


Open your browser and visit:

http://127.0.0.1:5000/


You can now add, edit, and delete users through the web interface.

Screenshots (Optional)

Add screenshots of the home page, add user form, and edit user form here to make your GitHub README more attractive.

Future Improvements

Add search functionality to find users quickly.

Add pagination for large user lists.

Implement login authentication to protect CRUD operations.

Switch to a more scalable database like MySQL or PostgreSQL.