from pyspark.sql import SparkSession
from graphframes import *

spark = SparkSession.builder.getOrCreate()

airports = spark.read.csv(r"newdata\airports.csv", header=True)
routes = spark.read.csv(r"newdata\routes.csv", header=True)

vertices = airports.withColumnRenamed("IATA", "airport")
edges = routes.withColumnRenamed("Source airport", "src").withColumnRenamed("Destination airport", "dst")

g = GraphFrame(vertices, edges)

results = g.shortestPaths(landmarks=["HND", "PUW"])

results.select("id", "distances").show()