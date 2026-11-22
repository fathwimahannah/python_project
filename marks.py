from database import get_connection


def add_mark():
    student_id_text = input("Enter student ID: ").strip()

    if not student_id_text.isdigit():
        print("Enter a valid student ID!")
        return

    student_id = int(student_id_text)
    subject = input("Enter subject: ").strip()
    mark_text = input("Enter mark (0-100): ").strip()

    if not subject:
        print("Subject cannot be empty!")
        return

    if not mark_text.isdigit() or not 0 <= int(mark_text) <= 100:
        print("Enter a mark between 0 and 100!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT student_id FROM students WHERE student_id = ?",
        (student_id,)
    )

    if not cursor.fetchone():
        print("Student not found!")
        conn.close()
        return

    cursor.execute("""
        INSERT INTO marks (student_id, subject, mark)
        VALUES (?, ?, ?)
    """, (student_id, subject, int(mark_text)))

    conn.commit()
    conn.close()
    print("Mark added successfully!")


def view_mark():
    student_id_text = input("Enter student ID: ").strip()

    if not student_id_text.isdigit():
        print("Enter a valid student ID!")
        return

    show_marks(int(student_id_text))


def show_marks(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT subject, mark
        FROM marks
        WHERE student_id = ?
    """, (student_id,))

    records = cursor.fetchall()

    if records:
        print("\n===== MARKS =====")
        for subject, mark in records:
            print(f"Subject: {subject} | Mark: {mark}")
    else:
        print("No marks found!")

    conn.close()