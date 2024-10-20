
# Exercise 3

import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'password',
    autocommit = True
)
def get_airport_name (ICAO):
    sql = f"select name from airport where ident = '{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    airport_name = cursor.fetchone()
    return airport_name

def get_location_by_ICAO (ICAO):
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{ICAO}'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return(result[0], result[1])
    else:
        print(f"No airport found with ICAO code: {ICAO}")
        return None
def calculate_distance_between_airport(code1,code2):
    cor1 = get_location_by_ICAO(code1)
    cor2 = get_location_by_ICAO(code2)
    if code1 and code2:
        distance = geodesic(cor1, cor2).kilometers
        print(f"The distance between {get_airport_name(code1)} and {get_airport_name(code2)} is {distance} km")


    else:
        print("unable to print the distance due to the missing data")
loc1 = input("Enter the first ICAO code: ")
loc2 = input("Enter the second ICAO code: ")
calculate_distance_between_airport(loc1, loc2)
connection.close()