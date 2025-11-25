# Flask + SQLite CRUD Application

## Project Overview

This project is a simple web application built with Flask and SQLite that allows users to Create, Read, Update, and Delete (CRUD) user records. It demonstrates how to integrate a Python backend with an SQLite database and a Bootstrap-powered frontend.

## Features

- **Add Users:** Input user details like Name, Contact, Address, Email, and Age.
- **View Users:** Display all users in a table format with serial numbers.
- **Edit Users:** Update all details of an existing user.
- **Delete Users:** Remove a user record with confirmation.
- **Flash Messages:** Shows success or warning messages when a user is added, updated, or deleted.
- **Responsive Design:** Uses Bootstrap 4 for a clean and responsive UI.

## Database

- **Database:** SQLite (`db_web.db`)
- **Table:** `users`

| Column | Type | Description |
|--------|------|-------------|
| UID | INTEGER PRIMARY KEY AUTOINCREMENT | Unique ID for each user |
| UNAME | TEXT | User’s full name |
| CONTACT | TEXT | Phone number or contact info |
| ADDRESS | TEXT | User address |
| EMAIL | TEXT | User email |
| AGE | INTEGER | User age |

*The table is created automatically if it does not exist.*

## How It Works

- **Homepage (`/` or `/index`):** Connects to SQLite database and fetches all users, displaying them in a table with options to Edit or Delete.
- **Add User (`/add_user`):** Opens a form to enter user details. On submit, it inserts the data into the database and shows a success flash message.
- **Edit User (`/edit_user/<uid>`):** Opens a form pre-filled with the selected user’s data. On submit, it updates the record in the database and shows a success flash message.
- **Delete User (`/delete_user/<uid>`):** Deletes the selected user from the database after confirmation and shows a warning flash message.
- **Flash Messages:** Used to inform the user about actions like adding, updating, or deleting a record.
- **Database Connection:** Each route connects to `db_web.db` using `sqlite3`. `row_factory = sqlite3.Row` is used for dictionary-style access in templates (e.g., `row['UNAME']`).

## Dependencies

- Python 3.x
- Flask
- SQLite (built into Python)
- Bootstrap 4 (via CDN in templates)

You can install Flask using:

```bash
pip install flask
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask_crud_project.git
   ```

2. Navigate to the project folder:
   ```bash
   cd flask_crud_project
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser and visit:
   ```<img width="730" height="613" alt="Screenshot 2025-11-25 194437" src="https://github.com/user-attachments/assets/13d41862-9499-4d25-8897-27d872b9fc35" />

   http://127.0.0.1:5000/
   ```

You can now add, edit, and delete users through the web interface.


