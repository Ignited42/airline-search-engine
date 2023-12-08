from pyspark.sql import SparkSession
from graphframes import *

spark = SparkSession.builder.getOrCreate()

airports = spark.read.csv(r"newdata\airports.csv", header=True)
routes = spark.read.csv(r"C:newdata\routes.csv", header=True)

vertices = airports.withColumnRenamed("IATA", "id")
edges = routes.withColumnRenamed("Source airport ID", "src").withColumnRenamed("Destination airport ID", "dst")

g = GraphFrame(vertices, edges)

results = g.shortestPaths(landmarks=["HND", "PUW"])

results.select("id", "distances").show()