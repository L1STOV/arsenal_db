import psycopg2

connection = psycopg2.connect(
    database="arsenal",
    user="postgres",
    password="",
    host="127.0.0.1",
    port="5432"
)

cur = connection.cursor()

cur.execute(
    "INSERT INTO transfers(date, player_first_name, player_second_name, transfer_type, from_club, to_club, price) "
    "VALUES ('2020-07-01', 'Cedric', 'Soares', 'Free transfer', 'Southampton', 'Arsenal', 'free');"
)

connection.commit()

print("-- Data insert --")

connection.close()
