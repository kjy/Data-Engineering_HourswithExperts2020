from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SparkPythonStarter").getOrCreate()

lines = spark.read.option("inferSchema", True).option("header", True).csv("people.txt")
lines.printSchema()

doubledAges = lines.select(col("name"), col("age")*2, col("dept"))
doubledAges.foreach(print)

averageAgeByDept = lines.groupBy(col("dept")).avg("age")
averageAgeByDept.foreach(print)







