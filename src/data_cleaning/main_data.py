# Authors: Mark, Steven, Yuuki
# Description:
<<<<<<< HEAD
#   Main file of source code
=======
#   Main file to run data cleaning and uploading processes
>>>>>>> 20682f71f38c148bcf2a462d380589da0177f043

import pandas as pd
import time
import os

import convertjson
<<<<<<< HEAD
import firebase
=======
import firestore
>>>>>>> 20682f71f38c148bcf2a462d380589da0177f043
import stats

airlines_df = convertjson.df_new1
airports_df = convertjson.df_new2
countries_df = convertjson.df_new3
planes_df = convertjson.df_new4
routes_df = convertjson.df_new5

times = list()
<<<<<<< HEAD

times.append(time.time())

firebase.create_collection(airlines_df, "Airlines")
times.append(time.time())

firebase.create_collection(airports_df, "Airports")
times.append(time.time())

firebase.create_collection(countries_df, "Countries")
times.append(time.time())

firebase.create_collection(planes_df, "Planes")
times.append(time.time())

firebase.create_collection(routes_df, "Routes")
=======
"""
times.append(time.time())

firestore.create_collection(airlines_df, "Airlines")
times.append(time.time())

firestore.create_collection(airports_df, "Airports")
times.append(time.time())

firestore.create_collection(countries_df, "Countries")
times.append(time.time())

firestore.create_collection(planes_df, "Planes")
times.append(time.time())
"""
print("Starting Routes collection")
firestore.create_collection(routes_df, "Routes")
>>>>>>> 20682f71f38c148bcf2a462d380589da0177f043
times.append(time.time())

try:
    os.mkdir("stats")
<<<<<<< HEAD
    outfile = open("stats/realtimedb_stats.txt", "w")
=======
    outfile = open("stats/firestore_stats.txt", "w")
>>>>>>> 20682f71f38c148bcf2a462d380589da0177f043

    stats.write_collection_stats(outfile, times)

    outfile.close()
except:
<<<<<<< HEAD
    outfile = open("realtimedb_stats.txt", "w")
=======
    outfile = open("firestore_stats.txt", "w")
>>>>>>> 20682f71f38c148bcf2a462d380589da0177f043
    stats.write_collection_stats(outfile, times)
    outfile.close()