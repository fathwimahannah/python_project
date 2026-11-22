import sqlite3
import hashlib
import os
import hmac
from database import get_connection


def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

    return salt.hex() + ":" + password_hash.hex()


def check_password(password, stored_password):
    salt_hex, hash_hex = stored_password.split(":")
    salt = bytes.fromhex(salt_hex)

    entered_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

    return hmac.compare_digest(entered_hash.hex(), hash_hex)


def admin_registration():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT login_id FROM login WHERE role = ?", ("admin",))
    if cursor.fetchone():
        print("An admin account already exists!")
        conn.close()
        return

    print("\n===== ADMIN REGISTRATION =====")
    username = input("Create admin username: ").strip()
    password = input("Create admin password: ")

    if not username or not password:
        print("Username and password cannot be empty!")
        conn.close()
        return

    try:
        cursor.execute("""
            INSERT INTO login (student_id, username, password, role)
            VALUES (NULL, ?, ?, 'admin')
        """, (username, hash_password(password)))

        conn.commit()
        print("Admin registered successfully!")

    except sqlite3.IntegrityError:
        print("That username is already used!")

    finally:
        conn.close()


def admin_login():
    username = input("Admin username: ").strip()
    password = input("Admin password: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT password FROM login
        WHERE username = ? AND role = 'admin'
    """, (username,))

    record = cursor.fetchone()
    conn.close()

    if record and check_password(password, record[0]):
        print("Admin login successful!")
        return True

    print("Invalid admin username or password!")
    return False


def student_registration():
    student_id_text = input("Enter your student ID: ").strip()

    if not student_id_text.isdigit():
        print("Enter a valid student ID!")
        return

    student_id = int(student_id_text)
    username = input("Create username: ").strip()
    password = input("Create password: ")

    if not username or not password:
        print("Username and password cannot be empty!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT student_id FROM students WHERE student_id = ?",
        (student_id,)
    )
    student = cursor.fetchone()

    if not student:
        print("Student ID not found. Ask the admin to register you first.")
        conn.close()
        return

    cursor.execute(
        "SELECT login_id FROM login WHERE student_id = ?",
        (student_id,)
    )
    if cursor.fetchone():
        print("This student already has a login account!")
        conn.close()
        return

    try:
        cursor.execute("""
            INSERT INTO login (student_id, username, password, role)
            VALUES (?, ?, ?, 'student')
        """, (student_id, username, hash_password(password)))

        conn.commit()
        print("Student account created successfully!")

    except sqlite3.IntegrityError:
        print("That username is already used!")

    finally:
        conn.close()


def student_login():
    username = input("Student username: ").strip()
    password = input("Student password: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, password FROM login
        WHERE username = ? AND role = 'student'
    """, (username,))

    record = cursor.fetchone()
    conn.close()

    if record and check_password(password, record[1]):
        print("Student login successful!")
        return record[0]

    print("Invalid student username or password!")
    return None