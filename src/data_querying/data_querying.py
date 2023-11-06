# Authors: Mark, Steven, Yuuki
# Description:
#   Queries data from Realtime DB.

from data_cleaning import firebase as fb
import math


def list_collection(collection_name, first_n):
    """
    Prints the "first_n" values in a collection given by "collection_name".\n
    Set "first_n" to NaN to print the entire collection.
    """

    collectionRef = fb.get_ref_collection(collection_name)

    try:
        if not math.isnan(first_n):
            collectionSnapshot = collectionRef.order_by_key().limit_to_first(first_n).get()
        else:
            collectionSnapshot = collectionRef.order_by_key().get()

        print(type(collectionSnapshot))

        for key,values in collectionSnapshot:
            print(key)
            print(values)
            print("---------")

    except:
        print("Invalid collection.")

    return
