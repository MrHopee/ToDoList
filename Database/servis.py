import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="ToDoList",
        user="postgres",
        password="umut123")

    print("connection successful")

    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except:
    print("connection unsuccessful")
