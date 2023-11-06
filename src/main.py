# Authors: Mark, Steven, Yuuki
# Description:
#   Main file to run source code

from data_operations import graph

#graph.create_graph()

routes = [{"help" : "me"}, {"hah" : "hoh"}]

if "help" not in routes:
    print("not in")
else:
    print("in")