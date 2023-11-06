# Authors: Mark, Steven, Yuuki
# Description:
#   Queries data from Realtime DB.

from data_cleaning import firebase as fb
import math


def list_collection(collection_name, first_n):
    """
    Prints the "first_n" values in a collection given by "collection_name".\n
    Set "first_n" to NaN to print the entire collection.\n\n

    Returns an ordered dict of the collection in question.
    """

    collectionRef = fb.get_ref_collection(collection_name)

    try:
        if not math.isnan(first_n):
            collectionSnapshot = collectionRef.order_by_key().limit_to_first(first_n).get()
        else:
            collectionSnapshot = collectionRef.order_by_key().get()

        print(type(collectionSnapshot))

        for key in collectionSnapshot:
            print(collectionSnapshot[key])

    except:
        print("Invalid collection.")

    return collectionSnapshot