# Author: Steven
# Description:
#   Uses Spark Dataframes to perform operations

import findspark
findspark.init()
from pyspark.sql import SparkSession

import pandas as pd

def getNeighbors(airportName, routesDF):
    """
    Get the neighboring airports to a given airport.
    
    ### Parameters
    - airportName: string
    - routesDF: pandas Dataframe, given by prepareRoutes()

    ### Returns
    - list of neighboring airports' names
    """
    spark = SparkSession.builder.appName("SparkOperations").getOrCreate()

    sparkDF = spark.createDataFrame(routesDF)

    sourceFiltered = sparkDF.filter(sparkDF["Source airport"] == airportName)\
                            .select("Destination airport").distinct()

    neighbors = list(sourceFiltered.toPandas().iloc[:,0])

    spark.stop()

    return neighbors

def prepareRoutes(routesList):
    """
    The routes list is in improper format to convert into a Spark Dataframe.
    This function prepares the list to a valid format.

    ### Parameter
    - routesList: the default Routes collection retrieved from MongoDB

    ### Returns
    A pandas Dataframe containing only:
    - Source airport name
    - Destination airport name

    ### Bugs
    Due to improper BSON handling, some entries are not stored properly when the data was
    uploaded onto the MongoDB database.  This results in non-standard schemas; some entries
    contain the incorrect field.
    """

    routesDF = pd.DataFrame(routesList)
    routesDF = routesDF.drop(columns=["_id","Codeshare","Airline"], axis=1)

    for x in routesDF.index:
        try:
            sourceName = routesDF.iloc[x]["Airports"]["Source"]["Name"]
            destName = routesDF.iloc[x]["Airports"]["Destination"]["Name"]
        except:
            sourceName = routesDF.iloc[x]["Airports"]["Source Name"]
            destName = routesDF.iloc[x]["Airports"]["Destination Name"]
        
        routesDF.at[x, "Source airport"] = sourceName
        routesDF.at[x, "Destination airport"] = destName

    routesDF = routesDF.drop(columns=["Airports","Stops"], axis=1)

    return routesDF

def getNeighborsList(airports, routesDF):
    """
    Returns a list of airports that are adjacent to the input `airports`.

    ### Parameters
    - airports: list of airport names (string)
    - routesDF: pandas Dataframe, given by prepareRoutes()
    """

    spark = SparkSession.builder.appName("SparkOperations").getOrCreate()

    sparkDF = spark.createDataFrame(routesDF)

    sourceFiltered = sparkDF.filter(sparkDF["Source airport"].isin(airports))\
                            .select("Destination airport").distinct()

    neighbors = list(sourceFiltered.toPandas().iloc[:,0])

    spark.stop()

    return neighbors