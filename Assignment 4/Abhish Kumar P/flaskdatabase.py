import sqlite3
conn = sqlite3.connect('students.db')
conn=sqlite3.connect('users.db')
print("Opened database successfully")
conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT,pin TEXT)')
conn.execute('CREATE TABLE users(name TEXT,email TEXT,phoneno TEXT,password TEXT)')
print("Table created successfully")
conn.close()