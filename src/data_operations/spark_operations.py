# Author: Steven
# Description:
#   Uses Spark Dataframes to perform operations

import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkOperations").getOrCreate()

def getNeighbors(airportName, routesList):
    

    return