from data_operations import graph
from utils import word_similarity as ws
import time

times = []

times.append(time.time())
print(ws.compare_words("alpha", "omega"))
times.append(time.time())

print(times[1]-times[0])
print(ws.compare_words("yar", "ryy"))
times.append(time.time())

print(times[2]-times[1])
print(ws.compare_words("help", "help_Bel"))

times.append(time.time())
print(ws.compare_words("woosh", "woo"))
times.append(time.time())