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

times.append(time.time())

print("Starting Airlines collection")
mongo.mongoDB_uploadCollection(airlines_df, "Airlines")
times.append(time.time())
print(times[-1] - times[-2])

print("Starting Airports collection")
mongo.mongoDB_uploadCollection(airports_df, "Airports")
times.append(time.time())
print(times[-1] - times[-2])

print("Starting Countries collection")
mongo.mongoDB_uploadCollection(countries_df, "Countries")
times.append(time.time())
print(times[-1] - times[-2])

print("Starting Planes collection")
mongo.mongoDB_uploadCollection(planes_df, "Planes")
times.append(time.time())
print(times[-1] - times[-2])

print("Starting Routes collection")
mongo.mongoDB_uploadCollection(routes_df, "Routes")
times.append(time.time())
print(times[-1] - times[-2])

try:
    os.mkdir("stats")
    outfile = open("stats/mongodb_stats.txt", "w")

    stats.write_collection_stats(outfile, times)

    outfile.close()
except:
    outfile = open("stats/mongodb_stats.txt", "w")
    stats.write_collection_stats(outfile, times)
    outfile.close()