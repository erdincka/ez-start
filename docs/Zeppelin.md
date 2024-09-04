# Zeppelin Notes

## Change port - conflicts with NFSv4 (ganesha)
zeppelin-env.sh - PORT


## Fix pyspark initialisation (is there a better way?)

```python
from py4j.java_gateway import java_import
java_import(spark._sc._jvm, "org.apache.spark.sql.api.python.*")
```

## Using Parquet and Hive

## Using Hive/parquet files

With example:

- `/opt/mapr/hive/hive-3.1.3/examples/files/data_with_valid_values.parquet`

Load data:

```sql
DROP TABLE parq;

CREATE TABLE parq(Col_INT32_UINT_8 INT, Col_INT32_UINT_16 INT, Col_INT32_UINT_32 INT, Col_INT64_UINT_64 BIGINT)
STORED AS PARQUET;

--- this will remove the file after successfull load
LOAD DATA INPATH 'maprfs:///apps/example_files/data_with_valid_values.parquet' INTO TABLE parq;


SELECT * from parq;


LOAD DATA LOCAL INPATH '/opt/mapr/hive/hive-3.1.3/examples/files/data_with_valid_values.parquet' INTO TABLE parq;


SELECT * from parq;
```

Using Avro/arrow files:

```sql
CREATE TABLE parquet_test
ROW FORMAT SERDE
   'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
OUTPUTFORMAT
   'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
TBLPROPERTIES (
  'avro.schema.url'='/hadoop/avro_events_scheme.avsc');

```

Or using Spark:

```spark

var df = spark.read.parquet("maprfs:///my_parquet_files/*.parquet");
df.write.mode(SaveMode.Overwrite).saveAsTable("imported_table")

```
