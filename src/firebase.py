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
    ref = db.reference(str(collection_name))

    for i in dataframe.index:
        try:  # Case where dataframe has column named 'Name'
            id = dataframe.iloc[i]['Name']
            ref.child(str(id)).update(dataframe.iloc[i].to_dict())
        except: # Case where dataframe doesn't have 'Name' column
            ref.child(str(i)).update(dataframe.iloc[i].to_dict())

    return