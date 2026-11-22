import sqlite3
from database import get_connection


def add_student():
    name = input("Enter name: ").strip()
    age_text = input("Enter age: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    course = input("Enter course: ").strip()

    if not name or not phone or not course:
        print("Name, phone, and course cannot be empty!")
        return

    if not age_text.isdigit() or int(age_text) <= 0:
        print("Enter a valid age!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO students (name, age, phone, email, course)
            VALUES (?, ?, ?, ?, ?)
        """, (name, int(age_text), phone, email, course))

        conn.commit()
        print("Student added successfully!")

    except sqlite3.IntegrityError:
        print("That phone number is already registered!")

    finally:
        conn.close()


def view_student():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if records:
        print("\n===== STUDENT DETAILS =====")
        for row in records:
            print(
                f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | "
                f"Phone: {row[3]} | Email: {row[4]} | Course: {row[5]}"
            )
    else:
        print("No student records found!")

    conn.close()


def search():
    student_id = input("Enter student ID: ").strip()

    if not student_id.isdigit():
        print("Enter a valid student ID!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (int(student_id),)
    )
    record = cursor.fetchone()

    if record:
        print("\n===== STUDENT FOUND =====")
        print("ID:", record[0])
        print("Name:", record[1])
        print("Age:", record[2])
        print("Phone:", record[3])
        print("Email:", record[4])
        print("Course:", record[5])
    else:
        print("Student not found!")

    conn.close()


def update_student():
    student_id = input("Enter student ID: ").strip()

    if not student_id.isdigit():
        print("Enter a valid student ID!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT student_id FROM students WHERE student_id = ?",
        (int(student_id),)
    )

    if not cursor.fetchone():
        print("Student not found!")
        conn.close()
        return

    name = input("Enter updated name: ").strip()
    age_text = input("Enter updated age: ").strip()
    phone = input("Enter updated phone: ").strip()
    email = input("Enter updated email: ").strip()
    course = input("Enter updated course: ").strip()

    if not name or not phone or not course:
        print("Name, phone, and course cannot be empty!")
        conn.close()
        return

    if not age_text.isdigit() or int(age_text) <= 0:
        print("Enter a valid age!")
        conn.close()
        return

    try:
        cursor.execute("""
            UPDATE students
            SET name = ?, age = ?, phone = ?, email = ?, course = ?
            WHERE student_id = ?
        """, (
            name, int(age_text), phone, email, course, int(student_id)
        ))

        conn.commit()
        print("Student updated successfully!")

    except sqlite3.IntegrityError:
        print("That phone number is already registered!")

    finally:
        conn.close()


def delete():
    student_id = input("Enter student ID: ").strip()

    if not student_id.isdigit():
        print("Enter a valid student ID!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM students WHERE student_id = ?",
        (int(student_id),)
    )
    record = cursor.fetchone()

    if not record:
        print("Student not found!")
        conn.close()
        return

    confirm = input(f"Delete {record[0]}? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Deletion cancelled!")
        conn.close()
        return

    try:
        cursor.execute(
            "DELETE FROM students WHERE student_id = ?",
            (int(student_id),)
        )
        conn.commit()
        print("Student deleted successfully!")

    except sqlite3.IntegrityError:
        print("Cannot delete this student because marks, attendance, or login records are linked to them.")

    finally:
        conn.close()


def view_my_details(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )
    record = cursor.fetchone()

    if record:
        print("\n===== MY DETAILS =====")
        print("ID:", record[0])
        print("Name:", record[1])
        print("Age:", record[2])
        print("Phone:", record[3])
        print("Email:", record[4])
        print("Course:", record[5])
    else:
        print("Student record not found!")

    conn.close()