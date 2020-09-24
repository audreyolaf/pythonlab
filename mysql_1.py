import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="olafolaf",
    database="olaf"
)
mycursor = mydb.cursor()
# INSERT
# sql = "INSERT INTO student (id, first_name, last_name, grade) VALUES (%s, %s, %s, %s)"
# val = (8, "Moana", "M", 11)

# SELECT, LIMIT
# mycursor.execute("SELECT * FROM student LIMIT 5")
# mycursor.execute("SELECT * FROM course")

# WHERE
# sql = "SELECT * FROM course WHERE teacher='Smith'"

# ORDER BY
# sql = "SELECT * FROM course ORDER BY teacher"

# DELETE
# sql = "DELETE FROM course WHERE id='1007'"

# DROP TABLE
# sql = "DROP TABLE students"

# UPDATE
# sql = "UPDATE student SET last_name = 'Chirp' WHERE first_name = 'Woodstock'"

# JOIN
sql = "SELECT \
  student.first_name AS s, \
  s_take_c.s_id AS sc \
  FROM student \
      INNER JOIN s_take_c ON student.id = s_take_c.s_id"

# sql = "SELECT \
#     course.name AS c, \
#     s_take_c.c_id AS sc \
#     FROM course \
#         INNER JOIN s_take_c ON course.id = s_take_c.c_id"

# sql = "SELECT s.*, c.* FROM student AS s, s_take_c. AS sc, course AS c WHERE s.id = sc.s_id AND c.id = sc.c_id"
# mycursor.execute(sql, val)  # INSERT
mycursor.execute(sql)  # WHERE, ORDER BY, DELETE, DROP TABLE, UPDATE, JOIN

# mydb.commit()  # INSERT, DELETE, UPDATE
# print(mycursor.rowcount, "record(s) affected")  # INSERT, DELETE, UPDATE
myresult = mycursor.fetchall()  # INSERt, SELECT, WHERE, ORDER BY
for x in myresult:  # SELECT, WHERE, ORDER BY
    print(x)
