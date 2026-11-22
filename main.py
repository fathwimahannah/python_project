from database import create_tables
from login import (
    admin_registration,
    admin_login,
    student_registration,
    student_login
)
from students import (
    add_student,
    view_student,
    search,
    update_student,
    delete,
    view_my_details
)
from marks import add_mark, view_mark, show_marks
from attendance import (
    add_attendance,
    view_attendance,
    show_attendance,
    attendance_percentage
)


def admin_menu():
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student") 
        print("5. Delete Student")
        print("6. Add Mark")
        print("7. View Marks")
        print("8. Add Attendance")
        print("9. View Attendance")
        print("10. Attendance Percentage")
        print("11. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete()
        elif choice == "6":
            add_mark()
        elif choice == "7":
            view_mark()
        elif choice == "8":
            add_attendance()
        elif choice == "9":
            view_attendance()
        elif choice == "10":
            attendance_percentage()
        elif choice == "11":
            print("Admin logged out!")
            break
        else:
            print("Invalid choice!")


def student_menu(student_id):
    while True:
        print("\n===== STUDENT MENU =====")
        print("1. View My Details")
        print("2. View My Marks")
        print("3. View My Attendance")
        print("4. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_my_details(student_id)
        elif choice == "2":
            show_marks(student_id)
        elif choice == "3":
            show_attendance(student_id)
        elif choice == "4":
            print("Student logged out!")
            break
        else:
            print("Invalid choice!")


def main_menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Admin Registration")
        print("2. Admin Login")
        print("3. Student Registration")
        print("4. Student Login")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            admin_registration()
        elif choice == "2":
            if admin_login():
                admin_menu()
        elif choice == "3":
            student_registration()
        elif choice == "4":
            student_id = student_login()
            if student_id is not None:
                student_menu(student_id)
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice!")


create_tables()
main_menu()