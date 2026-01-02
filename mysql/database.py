import pymysql
db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
)
print("Database connection established")

# i want to create a database named 'test_db'
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
print("Database 'test_db' created successfully")

# insert data into a table
cursor.execute("USE test_db")
cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    salary INT      
)""")
print("Table 'employees' created successfully")
# inserting data
cursor.execute("INSERT INTO employees (name, salary) VALUES ('rahul', 1000)")
cursor.execute("INSERT INTO employees (name, salary) VALUES ('sonam', 2000)")
cursor.execute("INSERT INTO employees (name, salary) VALUES ('anil', 3000)")
db.commit()

# fetching data
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()    
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Salary: {row[2]}")
# closing the connection
db.close()