# Author: Steven
# Description:
#   Purpose of file is to output proper JSON files to be ingested into a NoSQL document DB

import pandas as pd
import json

def create_collection(dframe):
    for x in dframe:
        print(x)


