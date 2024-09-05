# Using Hive for Delta

This assumes you have data in the cluster at `/tmp/clusters` in parquet format, with these fields:
```sql
_id varchar,
name varchar,
sex varchar,
country_code varchar,
```


## Create Hive table for customers

```sql
DROP TABLE hiveview.default.customers
```

```sql
CREATE TABLE hiveview.default.customers (
    _id varchar,
    name varchar,
    sex varchar,
    country_code varchar,
  )
  WITH (
    format = 'PARQUET',
    external_location = 'file:///tmp/customers/')

```

```sql
SELECT * FROM hiveview.default.customers LIMIT 10
```
