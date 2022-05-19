import psycopg2.extras

connection = None

try:
    connection = psycopg2.connect(
        host="localhost",
        database="ToDoList",
        user="postgres",
        password="umut123")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    print("connection successful")
except:
    print("connection unsuccessful")
