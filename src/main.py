# Authors: Mark, Steven, Yuuki
# Description:
#   Main file to run source code

#import data_querying.data_querying as dq
import firebase_admin
import time
from data_uploading import mongo

from data_operations import graph
from utils import word_similarity as ws