from  pyspark.sql import SparkSession

df=SparkSession.builder.appName("lrmod").getOrCreate()
