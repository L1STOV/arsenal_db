from db_config import cur
from db_config import connection

cur.execute('''
CREATE TABLE trophies(
id BIGSERIAL PRIMARY KEY,
trophies_name VARCHAR(50) NOT NULL,
times VARCHAR(5) NOT NULL,
season VARCHAR(10) NOT NULL,
wins VARCHAR(5) NOT NULL,
loses VARCHAR(5) NOT NULL,
draws VARCHAR(5) NOT NULL,
goal_difference VARCHAR(10) NOT NULL,
points VARCHAR(5) NOT NULL
);
''')

connection.commit()

