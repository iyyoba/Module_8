
# Exercise 2

import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'password',
    autocommit = True
)
def get_airport_by_area_code(local_code):
    sql = f"SELECT name, type FROM airport WHERE iso_country = %s ORDER BY type "

    cursor = connection.cursor()
    cursor.execute(sql, (local_code,))
    result = cursor.fetchall()
    return result if result else None

code = input(f"Enter the area code of the country or (type exit to quit): " )
airports = get_airport_by_area_code(code)

if airports:
    for airport_name, airport_type in airports:
        print(f"Airport_name: '{airport_name}' and Airport_type: '{airport_type}' ")
else:
    print("Not found for the given area code: ")