# Author: Steven
# Description:
#   Data upload to and import from MongoDB.

import pymongo

uri = "mongodb+srv://cluster0.pywaf93.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='./mongo_cert.pem',
                     server_api=pymongo.server_api.ServerApi('1'))

db = client["FlightToolApp"]

def mongoDB_ping():
    try:
        client.admin.command('ping')
        print("MongoDB successfully pinged!")
    except Exception as e:
        print(e)
    return

def mongoDB_uploadCollection(dataFrame, collectionName):
    collection = db[collectionName]

    print(dataFrame.head(4))
    data = dataFrame.to_dict(orient="records")
    result = collection.insert_many(data)
    print(result.inserted_ids)
    return