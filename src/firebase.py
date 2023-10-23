# Author(s): Steven
# Description:
#   Functions described here are designed to interface with the Realtime DB.

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('../credentials.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://flighttoolapp-default-rtdb.firebaseio.com'
})

def create_collection(dataframe, collection_name):

    return