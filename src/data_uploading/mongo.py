# Author: Steven Subianto
# Description:
#   Data upload to and import from MongoDB.

import pymongo

uri = "mongodb+srv://cluster0.pywaf93.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='./mongo_cert.pem',
                     server_api=ServerApi('1'))

