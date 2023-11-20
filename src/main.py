# Authors: Mark, Steven, Yuuki
# Description:
#   Main file to run source code

#import data_querying.data_querying as dq
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

from data_operations import graph
from utils import word_similarity as ws

"""
# Fetch the service account key JSON file contents
cred = credentials.Certificate('./credentials.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://flighttoolapp-default-rtdb.firebaseio.com'
})

#dq.list_collection("Planes", 5)

def ListAirline(n):
    airlineRef = db.reference('Airlines')
    airline_list = []

    snapshot = airlineRef.order_by_key().limit_to_first(n).get()

    for key in snapshot:
        airline_list.append(f"{snapshot[key]['Name']}")

    return airline_list

def ListAirport(n):
    airportRef = db.reference('Airports')
    airport_list = []

    snapshot = airportRef.order_by_key().limit_to_first(n).get()

    for key in snapshot:
        airport_list.append(f"{snapshot[key]['Name']}")

    return airport_list

def SerchAirport(input):
    airportRef = db.reference('Airports')

    snapshot = airportRef.order_by_key().equal_to(input).get()

    for key in snapshot:
        if key == input:
            print(f"City: {snapshot[key]['City']}") # Show City
            print(f"Country: {snapshot[key]['Country']['Name']}") # Show Country

def main():
    text = 'Tokyo Haneda International Airport'

    start_time = time.time()
    print("Airline: " + str(ListAirline(5)))
    end_time = time.time()
    print("Elapsed time (ListAirline()): " + str(end_time - start_time))
    
    start_time = time.time()
    print("Airport: " + str(ListAirport(5)))
    end_time = time.time()
    print("Elapsed time (ListAirport()): " + str(end_time - start_time))

    start_time = time.time()
    SerchAirport(text)
    end_time = time.time()
    print("Elapsed time (SerchAirport()): " + str(end_time - start_time))


if __name__ == "__main__":
    main()
"""

print(ws.compare_words("alpha", "omega"))

print(ws.compare_words("yar", "ryy"))

print(ws.compare_words("help", "help_Bel"))

print(ws.compare_words("woosh", "woo"))

print(ws.compare_words("sorry", "osrry"))