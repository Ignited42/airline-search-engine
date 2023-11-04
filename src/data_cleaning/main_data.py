# Authors: Mark, Steven, Yuuki
# Description:
#   Main file to run data cleaning and uploading processes

import pandas as pd
import time
import os

import convertjson
import firebase
import stats

airlines_df = convertjson.df_new1
airports_df = convertjson.df_new2
countries_df = convertjson.df_new3
planes_df = convertjson.df_new4
routes_df = convertjson.df_new5

times = list()

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
times.append(time.time())

try:
    os.mkdir("stats")
    outfile = open("stats/realtimedb_stats.txt", "w")

    stats.write_collection_stats(outfile, times)

    outfile.close()
except:
    outfile = open("realtimedb_stats.txt", "w")
    stats.write_collection_stats(outfile, times)
    outfile.close()