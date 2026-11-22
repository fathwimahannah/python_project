# Student Management System

### Python and SQLite College Project

## Project Overview

The Student Management System is a console-based application developed using Python and SQLite. It provides separate admin and student interfaces for managing student information, academic marks, and attendance records.

The system supports student registration, authentication, record management, and attendance percentage calculation.

## Admin Login Credentials

The following credentials are intended for the professor to test the admin functionality.

| Field | Value |
|---|---|
| Username | `hanna` |
| Password | `12345` |

**Note:** If the admin account has not been created in the database, select Admin Registration from the main menu and create the account using the above credentials. Then select Admin Login.

## How to Run the Project

1. Open the project folder in Visual Studio Code.
2. Open the terminal in the main project directory.
3. Run the following command:

```bash
python3 main.py
```

4. Select the required option from the main menu.
5. Use the admin credentials above to access the admin menu.

## Main Functionalities

### Admin Module

The administrator can:

- Register an admin account and log in.
- Add, view, search, update, and delete student records.
- Add and view student marks.
- Record and view student attendance.
- Calculate attendance percentages.
- Log out of the admin account.

### Student Module

Students can:

- Register an account using an existing student ID.
- Log in using their registered credentials.
- View their personal details.
- View their marks.
- View their attendance records.
- Log out of their account.

## Important System Rules

1. Each student is assigned a unique student ID automatically.
2. Student phone numbers and usernames must be unique.
3. Student accounts can only be registered after the administrator has added the student record.
4. Students can access only their own details, marks, and attendance records.
5. Marks must be entered between 0 and 100.
6. Attendance status must be either Present or Absent.
7. Attendance percentage is calculated using the number of present days divided by the total recorded attendance days.
8. Student records cannot be deleted if linked marks, attendance, or login records exist.
9. Admin passwords are stored as salted PBKDF2-HMAC-SHA256 hashes in the database.

## Project Structure

```text
Student Management System/
│
├── main.py
├── admin.py
├── login.py
├── database.py
├── students.py
├── marks.py
├── attendance.py
├── students.db
└── README.md
```

## Database

The application uses SQLite to store student information, login credentials, marks, and attendance records.

The database contains four tables:

| Table | Purpose |
|---|---|
| students | Stores student details |
| login | Stores user credentials and roles |
| marks | Stores academic marks |
| attendance | Stores attendance records |

The database and tables are initialized automatically when the application starts.

## Technologies Used

- Python 3
- SQLite
- Python SQLite3 module
- JSON is not used for database storage

## Project Information

**Project Type:** College Project

**Application:** Student Management System

**Language:** Python

**Database:** SQLite

