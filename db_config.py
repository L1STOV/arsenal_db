import psycopg2

connection = psycopg2.connect(
    database="arsenal",
    user="postgres",
    password="",
    host="127.0.0.1",
    port="5432"
)

cur = connection.cursor()

cur.execute('''CREATE TABLE transfers(
id BIGSERIAL PRIMARY KEY,
date DATE NOT NULL,
player_first_name VARCHAR(25) NOT NULL,
player_second_name VARCHAR(25) NOT NULL,
transfer_type VARCHAR(25) NOT NULL,
from_club VARCHAR(25) NOT NULL,
to_club VARCHAR(25) NOT NULL,
price VARCHAR(30)
);
''')