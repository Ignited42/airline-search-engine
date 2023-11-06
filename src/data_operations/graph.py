# Author(s): Steven
# Description:
#   Build a graph data structure to store locally and to execute
#   graphing algorithms such as shortest path.

import pandas as pd
import math
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

    # TODO: Still figuring out how to detect elements in a dict

    return routesGraph

def shortest_path(nodeA_name, nodeB_name, graph):
    """
    nodeA is the source node.  nodeB is the destination.
    """


    if nodeA_name == nodeB_name:
        return

    graphVisit = {}
    currentTentDistance = 0

    # Identify nodeA and nodeB, while creating graphVisit
    for node in graph:
        if node["Name"] == nodeA_name:
            nodeA = node
        
        if node["Name"] == nodeB_name:
            nodeB = node

        graphVisit.update({ node["Name"]: { "visited" : False, "tentDist" : math.inf, "prev": None}})

    # Check if nodes are properly set
    if nodeA is None or nodeB is None:
        print("A node doesn't exist.")
        return

    # Visit nodes
    currentNode = nodeA

    while currentNode is not None:
        nearestNeighbor = None

        for neighbor,dist in currentNode["Neighbor"]:
            neighborTentDist = graphVisit[neighbor]["tentDist"]
            graphVisit[neighbor]["tentDist"] = min(neighborTentDist, dist + currentTentDistance)

            if nearestNeighbor is None and not graphVisit[neighbor]["visited"]:
                nearestNeighbor = neighbor
            elif graphVisit[neighbor]["tentDist"] < graphVisit[nearestNeighbor["Name"]]["tentDist"]:
                nearestNeighbor = neighbor
        
        graphVisit[currentNode]["visited"] = True
        
        if nearestNeighbor is None or graphVisit[nearestNeighbor["Name"]]["tentDist"] == math.inf:
            currentNode = None
        else:
            currentNode = nearestNeighbor
            currentTentDistance = currentTentDistance + graphVisit[nearestNeighbor["Name"]]["tentDist"]

    # TODO: implement the "prev" calculation to return a path

    return

def save_graph(graph):
    """
    Saves a given graph.\n
    Note that a graph is a list of dicts, therefore can be stored as .json files.
    """