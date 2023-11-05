import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./credentials.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://flighttoolapp-default-rtdb.firebaseio.com'
})

ref = db.reference('Airports')

snapshot = ref.order_by_key().get()

for key in snapshot:
    print(key)