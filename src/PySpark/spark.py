from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("MongoDBIntegration") \
    .config("spark.mongodb.input.uri", "mongodb+srv://MarkSoze:piJcfEEYR0GbM0W6@ClusterO/FlightToolApp") \
    .config("spark.mongodb.output.uri", "mongodb+srv://MarkSoze:piJcfEEYR0GbM0W6@ClusterO/FlightToolApp") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:<VERSION>") \
    .getOrCreate()

# Load MongoDB collection into a DataFrame
flight_tool_app_df = spark.read.format("mongo").option("uri", "mongodb+srv://MarkSoze:piJcfEEYR0GbM0W6@ClusterO/FlightToolApp").load()

# Create separate DataFrames for each subsection
airlines_df = flight_tool_app_df.filter(flight_tool_app_df["category"] == "airlines")
airports_df = flight_tool_app_df.filter(flight_tool_app_df["category"] == "airports")
countries_df = flight_tool_app_df.filter(flight_tool_app_df["category"] == "countries")
planes_df = flight_tool_app_df.filter(flight_tool_app_df["category"] == "planes")
routes_df = flight_tool_app_df.filter(flight_tool_app_df["category"] == "routes")

# Show the DataFrames
airlines_df.show()
airports_df.show()
countries_df.show()
planes_df.show()
routes_df.show()
