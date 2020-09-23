from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("population").getOrCreate()

popDF = spark.read.json("data/population_data.json")
popDF.printSchema()

popDF.show()

max_year = popDF.select(col("Year")).sort(desc("Year")).take(1)
print(max_year)

min_year = popDF.select(col("Year")).sort(asc("Year")).take(1)
print(min_year)

num_count = popDF.select(col("Year"), col("Country Name"), col("Value")).filter("Year==1980").sort(desc("Value")).show()
income = popDF.select(col("Country Name")).contains("income").show()
print(income)