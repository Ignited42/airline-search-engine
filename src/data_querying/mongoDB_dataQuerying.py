# Authors: Mark, Steven, Yuuki
# Description:
#   Queries data from Mongo DB using Spark to handle parallel processing.

import findspark
findspark.init()

import pymongo
import pprint
from pyspark.sql import SparkSession

# Connecting to MongoDB using certificate
uri = "mongodb+srv://cluster0.pywaf93.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='./mongo_cert.pem',
                     server_api=pymongo.server_api.ServerApi('1'))

db = client["FlightToolApp"]

# Connecting to MongoDB using password
"""
uriSpark = "mongodb+srv://developer-2:HXxTrHl8gcVbLjSH@cluster0.pywaf93.mongodb.net/?retryWrites=true&w=majority"
spark = SparkSession.builder.appName("FlightToolApp") \
                    .config("spark.mongodb.read.connection.uri", uriSpark) \
                    .config("spark.mongodb.write.connection.uri", uriSpark) \
                    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.2.1") \
                    .getOrCreate()
"""
# ========================================================================

def getCollection(collectionName):
    """
    Retrieves a collection by its name from the remote MongoDB.

     - collectionName: name of a valid collection

    Returns the collection as a List.
    """
    try:
        #Spark implementation
        """ 
        dataFrame = spark.read.format("mongodb") \
                    .option("database", "FlightToolApp") \
                    .option("collection", collectionName).load()"""
        
        #Alt implementation
        collection = list(db[collectionName].find())
    except Exception as e:
        print(e)
    
    return collection

def listAirportsInCountry(countryName):
    """
    Returns a List of airport rows to a given country, by
    retrieving from MongoDB.
    """
    
    # First, check if country exists
    countryEntry = db["Countries"].find_one({"Name": countryName})
    airportsList = []
    
    # Next, deliver the list
    if countryEntry is not None:
        airportsColl = db["Airports"].find({"Country.Name": countryName})
        airportsList = list(airportsColl)

    return airportsList


"""
Reference code:
https://stackoverflow.com/questions/18501064/mongodb-aggregation-counting-distinct-fields
https://stackoverflow.com/questions/24761266/select-group-by-count-and-distinct-count-in-same-mongodb-query/24770233#24770233
https://stackoverflow.com/questions/13210730/how-to-make-pymongos-find-return-a-list
"""
def listBusiestCountries():
    """
    Returns a List of countries sorted by the number of airports.

    Done by retrieving from MongoDB and using their aggregation pipeline.
    """

    # Aggregate data to get busiest country by number of airports
    busyList = []

    pipeline = [
        {
            "$group": {
                "_id": { "Country": "$Country.Name" },
                "Count" : { "$sum": 1 },
                "Airports" : { "$addToSet": "$_id" }
            }
        },
        {
            "$sort": {
                "Count" : pymongo.DESCENDING
            }
        }
    ]

    try:
        busyList = list(db["Airports"].aggregate(pipeline))
    except Exception as e:
        print(e)

    return busyList