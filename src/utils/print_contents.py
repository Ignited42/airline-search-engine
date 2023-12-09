# Author: Steven
# Description:
#   Prints out the contents of given items.

def printAirport(airport):
    """
    Prints the contents of a document retrieved from Airports collection.
    """
    if airport == {}:
        return

    try:
        print("Name: " + str(airport["Name"]) + ", " + str(airport["Code"]["IATA"]))
        print("City: " + str(airport["City"]))
        print("Country: " + str(airport["Country"]["Name"]))
        print("Location:\n" + "\tLatitude: " + str(airport["Location"]["Latitude"]) +
                            "\n\tLongitude: " + str(airport["Location"]["Longitude"]))
    except Exception as e:
        print(e)

def printBusiestCountry(country):
    """
    Prints important content of countries given by listBusiestCountries().
    """

    try:
        countryName = country["_id"]["Country"]
        count = country["Count"]
        print("{countryName} - {count}")
    except Exception as e:
        print(e)