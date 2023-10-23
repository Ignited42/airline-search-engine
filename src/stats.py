# Author: Steven
# Description:
#   Functions defined here will write statistics into a given file.

import datetime

def write_collection_stats(outfile, time_list):
    outfile.write("Statistics taken on: " + str(datetime.datetime.now()) + "\n\n")
    i = 0
    prev = 0

    for time in time_list:
        outfile.write("\t" + str(i) + ": " + str(time) + "\t\tDifference from previous time: " + str(time - prev) + "\n")

        prev = time
        i = i + 1

    outfile.write("\nTotal time taken: " + str(time_list[-1] - time_list[0]))

    return