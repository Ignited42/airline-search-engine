# Authors: Mark, Steven, Yuuki
# Description:
#   Basic text menu to run functionality

from data_querying import mongoDB_dataQuerying as dataQuery
from data_operations import spark_operations as dataOp
from utils import print_contents as printHelper

routesDF = dataOp.prepareRoutes(dataQuery.getCollection("Routes", 0))

def run_main_menu():
    stopMenu = False
    while stopMenu != True:
        print("""
1. Search for airport
2. List airports in country
3. List busiest countries
4. See destinations

0. Exit application
""")

        userInput = input()
        inputInt = 0

        try:
            inputInt = int(userInput)
        except:
            continue

        match inputInt:
            case 1:
                run_case1()

            case 2:
                run_case2()
            
            case 3:
                run_case3()

            case 4:
                run_case4()

            case 0:
                stopMenu = True

def run_case1():
    """
    Runs the case where user searches for a specific airport.
    """

    stopMenu = False
    
    while stopMenu != True:
        print("""
Enter an empty string or 0 to go back.
Input the name of the airport:
""")
        userInput = input()

        if userInput == "" or userInput == "0":
            stopMenu = True
        else:
            airport = dataQuery.getAirportByName(userInput)
            printHelper.printAirport(airport)

def run_case2():
    """
    Runs the case where the user wants to list airports located on a country.
    """

    stopMenu = False
    
    while stopMenu != True:
        print("""
Enter an empty string or 0 to go back.
Input the name of a country:
""")
        userInput = input()

        if userInput == "" or userInput == "0":
            stopMenu = True
        else:
            airports = dataQuery.listAirportsInCountry(userInput, 0)
            maxIndex = min(len(airports),20)

            for i in range(maxIndex):
                print(f"{i + 1}: ")
                printHelper.printAirport(airports[i])

def run_case3():
    """
    Runs the case where the user wants to list the busiest countries, which is
    decided by the number of airports.
    """

    stopMenu = False
    countries = dataQuery.listBusiestCountries(0)

    minIndex = 0
    maxIndex = 20

    while stopMenu != True:
        try:
            print("Rank: Country Name - Number of Airports")
            for i in range(minIndex, maxIndex):
                country = countries[i]
                countryName = country["_id"]["Country"]
                count = country["Count"]
                print(f"{i + 1}: {countryName} - {count}")
        except Exception as e:
            print(e)
        
        print("""
Enter an empty string or 0 to go back.
Input a range of values to see certain ranges, example:
                                    `1 20` gives the first to twentieth busiest airport.
""")
        userInput = input()

        if userInput == "" or userInput == "0":
            stopMenu = True
        else:
            intInputs = userInput.split()

            try:
                newMin = int(intInputs[0]) - 1
                newMax = int(intInputs[1])

                minIndex = max(0, newMin)
                maxIndex = newMax
            except Exception as e:
                print(e)

def run_case4():
    """
    Runs the case where the user wants to list neighboring airports to a given airport.
    """

    stopMenu = False
    
    while stopMenu != True:
        print("""
Enter an empty string or 0 to go back.
Input the name of an airport:
""")
        userInput = input()

        if userInput == "" or userInput == "0":
            stopMenu = True
        else:
            neighbors = dataOp.getNeighbors(userInput, routesDF)
            print("Airports within one stop:")
            for neighbor in neighbors:
                print(f"\t{neighbor}")