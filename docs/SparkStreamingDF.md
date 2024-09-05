# Spark Streaming on DF

Note: all the examples below uses df20 as clustername, adjust accordingly.


## Ensure Spark configuration

Follow: https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/AdvancedInstallation/InstallSparkonYARN.html


`dnf install mapr-spark mapr-spark-historyserver mapr-spark-thriftserver`


Make sure to follow this if using Spark on YARN:

https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/Spark/ConfigureSparkJARLocation_2.0.1.html


## Set SPARK_HOME

`export SPARK_HOME=/opt/mapr/spark/spark-3.5.1`

## Create Stream

Run this on the cluster node

`maprcli stream create -path /apps/stream1 -produceperm p -consumeperm p -topicperm p`

## Install Delta library

`wget https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.2.0/delta-spark_2.12-3.2.0.jar`

## Save this code in cluster filesystem (ie, /mapr/CHANGEME/apps/spark-stream.py)


```python

from pyspark.sql import SparkSession
from pyspark.sql.types import StringType

mapr_user=
mapr_password=
hostname=
topic="/apps/stream1:topic1"


# Define Kafka parameters
kafka_params = {
    "kafka.bootstrap.servers": f"{hostname}:9092",
    "subscribe": topic,
    "startingOffsets": "earliest",
    "kafka.security.protocol": "SASL_PLAINTEXT",
    "kafka.sasl.mechanism": "PLAIN",
    "kafka.sasl.jaas.config": f'org.apache.kafka.common.security.plain.PlainLoginModule required username="{mapr_user}" password="{mapr_password}";'
}


def main():
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("KafkaToDelta") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .getOrCreate()

    # Read from Kafka and apply schema
    df = spark \
        .readStream \
        .format("kafka") \
        .options(**kafka_params) \
        .option("failOnDataLoss", "false") \
        .load() \
        .selectExpr("CAST(value AS STRING)") \
        .selectExpr("split(value, ',') as data") \
        .selectExpr(
            "cast(data[0] as int) as val0",
            "cast(data[1] as int) as val1",
            "cast(data[2] as int) as val2",
            "cast(data[3] as int) as val3",
        )

    # Define the Delta table path
    delta_table_path = "maprfs:///apps/delta_table_1/"

    # Define the checkpoint directory path
    checkpoint_dir = "maprfs:///apps/delta_checkpoint_1/"

    # Write the stream to the Delta table with a processing time trigger
    query = df \
        .writeStream \
        .format("delta") \
        .outputMode("append") \
        .trigger(processingTime="1 second") \
        .option("checkpointLocation", checkpoint_dir) \
        .option("mergeSchema", "true") \
        .option("overwrite", "true") \
        .start(delta_table_path)

    # Start the streaming query
    query.awaitTermination(180)

if __name__ == "__main__":
    main()

```


## Submit this script to Spark on YARN

```bash


$SPARK_HOME/bin/spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --packages io.delta:delta-spark_2.12:3.2.0 \
    --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
    --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
    --conf spark.driver.cores=1 \
    --conf spark.driver.memory=1G \
    --conf spark.executor.instances=1 \
    --conf spark.executor.cores=1 \
    --conf spark.executor.memory=1G \
    maprfs:///apps/spark-stream.py

```
