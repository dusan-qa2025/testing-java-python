import mysql.connector as conn
import json

connection = conn.connect(
    host="localhost", 
    user="root",
    password = "Dusan-qa-tester", # Unesi svoj password
    database = "sakila"
)


kursor = connection.cursor()
kursor.execute(" select title, release_year from film limit 10;")
filmovi = kursor.fetchall()

print("filmovi u ponudi:")
for title, release_year in filmovi:
    print(f"NAME: {title}, YEAR: {release_year}")


json_podaci = json.dumps(filmovi, indent=4)
print(json_podaci)

connection.close()