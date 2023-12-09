# Authors: Mark, Steven, Yuuki
# Description:
#   Main file to run data cleaning and uploading processes

import pandas as pd
import time
import os

from data_cleaning import convertjson
from data_uploading import mongo
from data_uploading import stats

airlines_df = convertjson.df_new1
airports_df = convertjson.df_new2
countries_df = convertjson.df_new3
planes_df = convertjson.df_new4
routes_df = convertjson.df_new5

times = list()

isLocal = 1

times.append(time.time())

print("Starting Airlines collection")
mongo.uploadCollection(airlines_df, "Airlines", isLocal)
times.append(time.time())
print(times[-1] - times[-2])

print("Starting Airports collection")
mongo.uploadCollection(airports_df, "Airports", isLocal)
times.append(time.time())
print(times[-1] - times[-2])

print("Starting Countries collection")
mongo.uploadCollection(countries_df, "Countries", isLocal)
times.append(time.time())
print(times[-1] - times[-2])

print("Starting Planes collection")
mongo.uploadCollection(planes_df, "Planes", isLocal)
times.append(time.time())
print(times[-1] - times[-2])

print("Starting Routes collection")
mongo.uploadCollection(routes_df, "Routes", isLocal)
times.append(time.time())
print(times[-1] - times[-2])

try:
    os.mkdir("stats")
    outfile = open("stats/mongodb_local_stats.txt", "w")

    stats.write_collection_stats(outfile, times)

    outfile.close()
except:
    outfile = open("stats/mongodb_local_stats.txt", "w")
    stats.write_collection_stats(outfile, times)
    outfile.close()