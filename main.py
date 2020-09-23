import psycopg2

connection = psycopg2.connect(
    database="arsenal",
    user="postgres",
    password="",
    host="127.0.0.1",
    port="5432"
)

print("Database opened")
cursor = connection.cursor()
