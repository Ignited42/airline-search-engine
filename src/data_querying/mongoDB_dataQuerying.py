# Authors: Mark, Steven, Yuuki
# Description:
#   Queries data from Mongo DB using Spark to handle parallel processing.

import findspark
findspark.init()

import pymongo
import pprint
from pyspark.sql import SparkSession

"""
Remote DB, indexed as 0 for variables: `client` and `db`
"""
uri = "mongodb+srv://cluster0.pywaf93.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = { 0: pymongo.MongoClient(uri,
                                tls=True,
                                tlsCertificateKeyFile='./mongo_cert.pem',
                                server_api=pymongo.server_api.ServerApi('1'))}

db = { 0: client[0]["FlightToolApp"]}

"""
Local DB, indexed as 1 for variables: `client` and `db`
"""
localUri = "mongodb://localhost:27017"
try:
    client = { 1: pymongo.MongoClient(localUri) }
    db = { 1: client[1]["FlightToolApp"] }
except Exception as e:
    print(e)

"""spark = SparkSession.builder.appName("FlightToolApp") \
                            .config("spark.mongodb.read.connection.uri", localUri + str("/test.coll")) \
                            .config("spark.mongodb.write.connection.uri", localUri + str("/test.coll")) \
                            .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.2.1") \
                            .getOrCreate()"""

# ========================================================================

def getCollection(collectionName, isLocal):
    """
    Retrieves a collection by its name from the remote MongoDB.

    ### Parameters
    - collectionName: name of a valid collection
    - isLocal: determines if the mongoDB server is the remote (0) or local (1) one
     
    ### Returns
    Returns the collection as a List.
    """
    if isLocal != 0 and isLocal != 1:
        return 

    collection = []

    try:
        """
        #Spark implementation
        if isLocal == 1:
            dataFrame = spark.read.format("mongodb") \
                        .option("database", "FlightToolApp") \
                        .option("collection", collectionName).load()
            
            dataFrame.printSchema()
            dataFrame.show()

        #Alt implementation
        else:
            collection = list(db[isLocal][collectionName].find())    
        """
        collection = list(db[isLocal][collectionName].find())    
        
    except Exception as e:
        print(e)
    
    return collection

def listAirportsInCountry(countryName, isLocal):
    """
    Returns a List of airport rows to a given country, by retrieving from MongoDB.

    ### Parameters
    - countryName: string
    - isLocal: determines if the mongoDB server is the remote (0) or local (1) one
    """
    if isLocal != 0 and isLocal != 1:
        return     

    
    # First, check if country exists
    countryEntry = db[isLocal]["Countries"].find_one({"Name": countryName})
    airportsList = []
    
    # Next, deliver the list
    if countryEntry is not None:
        airportsColl = db[isLocal]["Airports"].find({"Country.Name": countryName})
        airportsList = list(airportsColl)

    return airportsList


"""
Reference code:
https://stackoverflow.com/questions/18501064/mongodb-aggregation-counting-distinct-fields
https://stackoverflow.com/questions/24761266/select-group-by-count-and-distinct-count-in-same-mongodb-query/24770233#24770233
https://stackoverflow.com/questions/13210730/how-to-make-pymongos-find-return-a-list
"""
def listBusiestCountries(isLocal):
    """
    Returns a List of countries sorted by the number of airports.\n
    Done by retrieving from MongoDB and using their aggregation pipeline.

    ### Parameters
    - isLocal: determines if the mongoDB server is the remote (0) or local (1) one
    """
    if isLocal != 0 and isLocal != 1:
        return 

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
        busyList = list(db[isLocal]["Airports"].aggregate(pipeline))
    except Exception as e:
        print(e)

    return busyList