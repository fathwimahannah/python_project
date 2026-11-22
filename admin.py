import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM login WHERE role = 'admin'")

conn.commit()
conn.close()

print("Admin account reset. You can register a new admin now.")