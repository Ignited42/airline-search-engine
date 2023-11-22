# Authors: Mark, Steven, Yuuki
# Description:
#   Queries data from Realtime DB.

import firebase_admin as fb
from firebase_admin import db
from firebase_admin import credentials
import math

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./credentials.json')

# Initialize the app with a service account, granting admin privileges
fb.initialize_app(cred, {
    'databaseURL': 'https://flighttoolapp-default-rtdb.firebaseio.com'
})


def list_collection(collection_name, first_n):
    """
    Prints the "first_n" values in a collection given by "collection_name".\n
    Set "first_n" to NaN to print the entire collection.
    """

    collectionRef = fb.get_ref_collection(collection_name)

    try:
        if not math.isnan(first_n):
            collectionSnapshot = collectionRef.order_by_key().limit_to_first(first_n).get()
        else:
            collectionSnapshot = collectionRef.order_by_key().get()

        print(type(collectionSnapshot))

        for key,values in collectionSnapshot:
            print(key)
            print(values)
            print("---------")

    except:
        print("Invalid collection.")

    return

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

def SearchAirport(input):
    airportRef = db.reference('Airports')

    snapshot = airportRef.order_by_key().equal_to(input).get()

    for key in snapshot:
        if key == input:
            print(f"City: {snapshot[key]['City']}") # Show City
            print(f"Country: {snapshot[key]['Country']['Name']}") # Show Country


"""

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
    SearchAirport(text)
    end_time = time.time()
    print("Elapsed time (SerchAirport()): " + str(end_time - start_time))


if __name__ == "__main__":
    main()
"""