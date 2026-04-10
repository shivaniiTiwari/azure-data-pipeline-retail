# Databricks notebook source
df.write.mode("overwrite") \
        .option("header", "true") \
            .csv("abfss://raw-data@datalakeshivani01.dfs.core.windows.net/output/orders_csv")


# COMMAND ----------

df.show(5)

# COMMAND ----------

df = spark.read.format("delta") \
            .load("abfss://raw-data@datalakeshivani01.dfs.core.windows.net/processed/orders")

# COMMAND ----------

spark.conf.set(
          "fs.azure.account.key.datalakeshivani01.dfs.core.windows.net",
                  "<your-storage-key>"
                          )


# COMMAND ----------

df = spark.read.format("delta") \
        .load("abfss://raw-data@datalakeshivani01.dfs.core.windows.net/processed/orders")


# COMMAND ----------

df_daily_sales = df.groupBy("order_date") \
        .sum("sales") \
            .orderBy("order_date")

df_daily_sales.show()


# COMMAND ----------

df_region_sales = df.groupBy("region") \
        .sum("sales")

df_region_sales.show()
        

# COMMAND ----------

df.write.format("delta") \
        .mode("overwrite") \
            .save("abfss://raw-data@datalakeshivani01.dfs.core.windows.net/processed/orders")


# COMMAND ----------

df = df.drop("c")


# COMMAND ----------

df.printSchema()


# COMMAND ----------

df = spark.read.format("csv") \
        .option("header", "true") \
            .option("inferSchema", "true") \
                .option("quote", '"') \
                    .option("escape", '"') \
                        .option("multiLine", "true") \
                            .load("abfss://raw-data@datalakeshivani01.dfs.core.windows.net/orders.csv")


# COMMAND ----------

df.printSchema()
df.select("sales").show(5)


# COMMAND ----------

df = df.filter("sales IS NOT NULL")


# COMMAND ----------

from pyspark.sql.functions import expr

df = df.withColumn("sales", expr("try_cast(sales as double)"))


# COMMAND ----------

df.printSchema()


# COMMAND ----------

from pyspark.sql.functions import col

df = df.withColumn("sales", col("sales").cast("double"))


# COMMAND ----------

df.printSchema()

# COMMAND ----------

df = spark.read.format("csv") \
        .option("header", "true") \
            .option("inferSchema", "true") \
                .load("abfss://raw-data@datalakeshivani01.dfs.core.windows.net/orders.csv")


# COMMAND ----------

display(dbutils.fs.ls("abfss://raw-data@datalakeshivani01.dfs.core.windows.net/"))


# COMMAND ----------

spark.conf.set(
      "fs.azure.account.key.datalakeshivani01.dfs.core.windows.net",
        "<your-storage-key>"
        )

