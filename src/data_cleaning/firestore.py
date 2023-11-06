# Author: Steven
# Description:
#   The functions defined in this file will upload collections and documents into the Firestore DB.

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

# Initialize credentials and application
cred = credentials.Certificate("./credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()


def create_collection(dataframe, collection_name):
    coll_ref = db.collection(collection_name)
    
    for i in dataframe.index:
        try: # Case where Dataframe has column "Name"
            coll_ref.document(str(dataframe.iloc[i]["Name"])).set(dataframe.iloc[i].to_dict())
        except: # Case where Dataframe doesn't have column "Name"
            coll_ref.document(str(i)).set(dataframe.iloc[i].to_dict())
    return