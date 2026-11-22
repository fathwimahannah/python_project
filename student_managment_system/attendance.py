from datetime import date
from database import get_connection


def add_attendance():
    student_id_text = input("Enter student ID: ").strip()

    if not student_id_text.isdigit():
        print("Enter a valid student ID!")
        return

    student_id = int(student_id_text)
    status = input("Enter attendance (Present/Absent): ").strip().lower()

    if status not in ["present", "absent"]:
        print("Enter Present or Absent!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM students WHERE student_id = ?",
        (student_id,)
    )
    student = cursor.fetchone()

    if not student:
        print("Student not found!")
        conn.close()
        return

    cursor.execute("""
        INSERT INTO attendance (student_id, date, status)
        VALUES (?, ?, ?)
    """, (student_id, date.today().isoformat(), status.capitalize()))

    conn.commit()
    conn.close()
    print("Attendance added successfully!")


def view_attendance():
    student_id_text = input("Enter student ID: ").strip()

    if not student_id_text.isdigit():
        print("Enter a valid student ID!")
        return

    show_attendance(int(student_id_text))


def show_attendance(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT date, status
        FROM attendance
        WHERE student_id = ?
        ORDER BY date
    """, (student_id,))

    records = cursor.fetchall()

    if records:
        print("\n===== ATTENDANCE =====")
        for record_date, status in records:
            print(f"Date: {record_date} | Status: {status}")
    else:
        print("No attendance records found!")

    conn.close()


def attendance_percentage():
    student_id_text = input("Enter student ID: ").strip()

    if not student_id_text.isdigit():
        print("Enter a valid student ID!")
        return

    student_id = int(student_id_text)
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status
        FROM attendance
        WHERE student_id = ?
    """, (student_id,))

    records = cursor.fetchall()
    conn.close()

    if not records:
        print("No attendance records found!")
        return

    total_days = len(records)
    present_days = sum(1 for row in records if row[0] == "Present")
    percentage = (present_days / total_days) * 100

    print("\n===== ATTENDANCE REPORT =====")
    print("Total days:", total_days)
    print("Present days:", present_days)
    print("Absent days:", total_days - present_days)
    print("Attendance percentage:", round(percentage, 2), "%")