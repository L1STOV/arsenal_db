import psycopg2

connection = psycopg2.connect(
    database="arsenal",
    user="postgres",
    password="",
    host="127.0.0.1",
    port="5432"
)

cur = connection.cursor()

connection.commit()

print("-- Data insert --")

connection.close()
