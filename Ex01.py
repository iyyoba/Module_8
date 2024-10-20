
# Exercise 1

import mysql.connector

connection = mysql.connector.connect (
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='password',
    autocommit=True
)
def get_airport_info_by_ident (ICAO):
    sql = "select name,municipality from airport where ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (ICAO,) )
    result = cursor.fetchone()
    return result if result else None

while True:
    code = input("Enter ICAO code or press exit to quite ")

    if code.lower == "exit":
        break
    airport_info = get_airport_info_by_ident (code)

    if airport_info:
        Airport_name,Town = airport_info
        print(f"Airport Name and Town is: {airport_info} ")
    else:
        print("There is no airport name with this CIAO: ")