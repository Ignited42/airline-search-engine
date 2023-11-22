# Author: Steven Subianto
# Description:
#   Data upload to and import from MongoDB.

import pymongo

uri = "mongodb+srv://cluster0.pywaf93.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='./mongo_cert.pem',
                     server_api=pymongo.server_api.ServerApi('1'))

def mongoDB_ping():
    try:
        client.admin.command('ping')
        print("MongoDB successfully pinged!")
    except Exception as e:
        print(e)
    return

def mongoDB_uploadCollection(collectionName):
    
    return