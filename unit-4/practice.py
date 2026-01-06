import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="students",
    user="postgres",
    password="macmhn1"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS student_marks (
    id SERIAL PRIMARY KEY,
    subject VARCHAR(50),
    marks INT
)
""")
conn.commit()

cur.execute("""
INSERT INTO student_marks (subject, marks) VALUES
('Maths', 85),
('Physics', 78),
('Chemistry', 88),
('Biology', 90),
('English', 75),
('Computer', 92),
('History', 70),
('Geography', 74),
('Economics', 80),
('Civics', 68),
('Maths', 89),
('Physics', 82),
('Chemistry', 91),
('Biology', 87),
('English', 76),
('Computer', 95),
('History', 72),
('Geography', 77),
('Economics', 83),
('Civics', 69);
""")

conn.commit()
print("20 records inserted successfully")
cur.execute("SELECT * FROM student_marks")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()