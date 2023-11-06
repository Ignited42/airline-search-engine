# Authors: Mark, Steven, Yuuki
# Description:
#   Main file to run source code

#import data_querying.data_querying as dq
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./credentials.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://flighttoolapp-default-rtdb.firebaseio.com'
})

#dq.list_collection("Planes", 5)

def ListAirline():
    airlineRef = db.reference('Airlines')

    snapshot = airlineRef.order_by_key().get()

    for key in snapshot:
        print(key) # Print all

def ListAirport():
    airportRef = db.reference('Airports')

    snapshot = airportRef.order_by_key().get()

    for key in snapshot:
        print(key) # Print all

def SerchAirport(input):
    airportRef = db.reference('Airports')

    snapshot = airportRef.order_by_key().get()

    for key in snapshot:
        if key == input:
            print(f"City: {snapshot[key]['City']}") # Show City
            print(f"Country: {snapshot[key]['Country']['Name']}") # Show Country

def main():
    text = 'Tokyo Haneda International Airport'

    ListAirline()
    ListAirport()
    SerchAirport(text)

if __name__ == "__main__":
    main()