# Author: Steven
# Description:
#   Data upload to and import from MongoDB.

import pymongo

"""
Remote DB, indexed as 0 for variables: `client` and `db`
"""
uri = "mongodb+srv://cluster0.pywaf93.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = { 0: pymongo.MongoClient(uri,
                                    tls=True,
                                    tlsCertificateKeyFile='./mongo_cert.pem',
                                    server_api=pymongo.server_api.ServerApi('1')) }

db = { 0: client[0]["FlightToolApp"] }

"""
Local DB, indexed as 1 for variables: `client` and `db`
"""
localUri = "mongodb://localhost:27017"
try:
    client.update({ 1: pymongo.MongoClient(localUri) })
    db.update({ 1: client[1]["FlightToolApp"] })
except Exception as e:
    print(e)

# ======================================================================

def ping(isLocal):
    """
    Pings to a mongoDB server.

    ### Parameters:
    - isLocal: determines if the mongoDB server is the remote (0) or local (1) one
    """
    if isLocal != 0 and isLocal != 1:
        return 

    try:
        client[isLocal].admin.command('ping')
        print("MongoDB successfully pinged!")
    except Exception as e:
        print(e)
    return

def uploadCollection(dataFrame, collectionName, isLocal):
    """
    Uploads a given dataFrame as a collection to a mongoDB server.

    ### Parameters:
    - dataFrame: a pandas dataFrame 
    - collectionName: a string
    - isLocal: determines if the mongoDB server is the remote (0) or local (1) one
    """
    if isLocal != 0 and isLocal != 1:
        return

    collection = db[isLocal][collectionName]

    print(dataFrame.head(4))
    data = dataFrame.to_dict(orient="records")
    result = collection.insert_many(data)
    print(result.inserted_ids)
    return