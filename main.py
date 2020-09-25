from db_config import connection
from db_config import cur

try:
    cur.execute("SELECT * FROM transfers WHERE from_club = 'Arsenal' ORDER BY to_club, date;")

    rows = cur.fetchall()

    for row in rows:
        print("\nTransfer date -", row[1])
        print("Players name -", row[2], row[3])
        print("Transfer type -", row[4])
        print("From -", row[5])
        print("To -", row[6])
        print("Price -", row[7])

except Exception as error:
    print("\n---Query is failed -", error, '---\n')
finally:
    connection.close()
    print("\n---Connection to database is closed---\n")
