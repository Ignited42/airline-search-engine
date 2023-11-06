# Authors: Mark, Steven, Yuuki
# Description:
#   Main file to run source code

from data_operations import graph
from utils import word_similarity as ws

print(ws.compare_words("alpha", "omega"))

print(ws.compare_words("yar", "ryy"))

print(ws.compare_words("help", "help_Bel"))

print(ws.compare_words("woosh", "woo"))