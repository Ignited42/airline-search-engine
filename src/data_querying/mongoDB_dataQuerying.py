# Authors: Mark, Steven, Yuuki
# Description:
#   Queries data from Mongo DB using Spark to handle parallel processing.

import findspark
findspark.init()

import pymongo
import pprint
from pyspark.sql import SparkSession

uri = "mongodb+srv://cluster0.pywaf93.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='./mongo_cert.pem',
                     server_api=pymongo.server_api.ServerApi('1'))

db = client["FlightToolApp"]

"""spark = SparkSession.builder.appName("FlightToolApp") \
                    .config("spark.mongodb.input.connection.uri", uri) \
                    .config("spark.mongodb.output.connection.uri", uri) \
                    .getOrCreate()"""

def getCollection(collectionName):
    try:
        #Spark implementation
        """dataFrame = spark.read.format("mongodb") \
                    .option("database", "FlightToolApp") \
                    .option("collection", collectionName).load()"""
        
        #Alt implementation
        collection = db[collectionName].find()
    except Exception as e:
        print(e)
    
    return collection

def listAirportsInCountry(countryName):
    # First, check if country exists
    countryEntry = db["Countries"].find_one({"Name": countryName})
    airportsList = []
    
    # Next, deliver the list
    if countryEntry is not None:
        airportsColl = db["Airports"].find({"Country.Name": countryName})
        for entry in airportsColl:
            airportsList.append(entry)

    return airportsList


"""
Reference code:
https://stackoverflow.com/questions/18501064/mongodb-aggregation-counting-distinct-fields
https://stackoverflow.com/questions/24761266/select-group-by-count-and-distinct-count-in-same-mongodb-query/24770233#24770233
"""
def getBusiestCountry():
    # Aggregate data to get busiest country by number of airports
    busyList = []

    pipeline = [
        {
            "$group": { "_id": { } }
        }
    ]


    return