# Author: Steven
# Description:
#   Uses Spark Dataframes to perform operations

import findspark
findspark.init()
from pyspark.sql import SparkSession

import pandas as pd

spark = SparkSession.builder.getOrCreate()

def getNeighbors(airportName, routesDF):
    """
    Get the neighboring airports to a given airport.
    
    ### Parameters
    - airportName: string
    - routesDF: pandas Dataframe, given by prepareRoutes()

    ### Returns
    - list of neighboring airports' names
    """

    sparkDF = spark.createDataFrame(routesDF)

    sourceFiltered = sparkDF.filter(sparkDF["Source airport"] == airportName)\
                            .select("Destination airport").distinct()

    neighbors = list(sourceFiltered.toPandas().iloc[:,0])

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
    Returns a Spark Dataframe of airports that are adjacent to the input `airports`.

    ### Parameters
    - airports: list of airport names (string)
    - routesDF: pandas Dataframe, given by prepareRoutes()

    ### Returns
    A Spark Dataframe, containing one column; that is the list of airports adjacent
    to the input `airports`. 
    """

    sparkDF = spark.createDataFrame(routesDF)

    sourceFiltered = sparkDF.filter(sparkDF["Source airport"].isin(airports))\
                            .select("Destination airport").distinct()

    return sourceFiltered

def withinNHops(airport, nHops, routesDF):
    """
    Given an airport, what destinations are reachable within N hops?

    ### Parameters
    - airport: name of airport (string)
    - nHops: number of hops (int)
    - routesDF: pandas Dataframe, given by prepareRoutes()

    ### Returns
    A dict `{n: [airports], ...}` where `n` is the exact number of hops it takes
    to reach the list of airports: `[airports]`.

    ### Bugs
    Currently doesn't work.
    """

    dFList = {}
    airports = [airport]

    if nHops is not int and nHops <= 0:
        return
    else:
        # Create DataFrame version of the dict first
        for hop in range(nHops):
            currDF = getNeighborsList(airports, routesDF)

            if len(dFList) > 0:
                cumulPrevDF = dFList[1]
                for prev in range(1, len(dFList)):
                    prevDF = dFList[prev + 1]
                    cumulPrevDF = cumulPrevDF.union(prevDF).distinct()

                currDF = currDF.subtract(cumulPrevDF)
            
            dFList.update({ (hop+1): currDF })

            airports = list(dFList[hop+1].toPandas().iloc[:,0])
        
        # Create list version of dict
        nHopsList = {0: [airport]}

        for hop in range(len(dFList)):
            nHopsList.update({ (hop+1): list(dFList[hop+1].toPandas().iloc[:,0]) })

    return nHopsList
