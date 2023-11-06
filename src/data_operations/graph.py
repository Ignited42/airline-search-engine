# Author(s): Steven
# Description:
#   Build a graph data structure to store locally and to execute
#   graphing algorithms such as shortest path.

import pandas as pd
from data_querying import data_querying as dq

def create_graph():
    """
    Creates a graph from the given routes.\n
    \t  Nodes/vertices in the graph are dicts, containing the following:\n
    \t  1. Name\n
    \t  2. ID\n
    \t  3. Adjacent nodes; in dicts\n
    \t\t    Key: ID of neighbor\n
    \t\t    Value: distance\n

    Returns a list of dicts.
    """

    routesGraph = []

    routesColl = dq.list_collection("Routes", 5)

    # Set nodes of graph
    for route in routesColl:
        sourceAirport = route["Airports"]["Source"]
        destinationAirport = route["Airports"]["Destination"]

    return routesGraph

def shortest_path(nodeA, nodeB):
    


    return

def save_graph(graph):
    """
    Saves a given graph.\n
    Note that a graph is a list of dicts, therefore can be stored as .json files.
    """