# KSQL

[Installation](https://docs.ezmeral.hpe.com/datafabric-customer-managed/76/Kafka/KSQL/Ksql-demo-example.html)


`maprcli stream create -path /kafkatest -produceperm p -consumeperm p -topicperm p`

`cd /opt/mapr/ksql/ksql-7.6.0`

`./bin/ksql-datagen quickstart=pageviews format=delimited topic=/kafkatest:pageviews maxInterval=10000`

`./bin/ksql https://CHANGEME:8084`

```sql
CREATE STREAM pageviews
        (viewtime BIGINT,
         userid VARCHAR,
         pageid VARCHAR)
         WITH (KAFKA_TOPIC='/kafkatest:pageviews',
         VALUE_FORMAT='DELIMITED');
```


```sql
CREATE TABLE PAGEVIEWS_TABLE
         WITH(KAFKA_TOPIC='/kafkatest:pageviews')
         AS
           SELECT userid,
           MAX(viewtime)
           FROM pageviews
           GROUP BY userid;
```

```sql
SHOW STREAMS;
```

```sql
SHOW TABLES;
```

```sql
SELECT * FROM PAGEVIEWS_TABLE WHERE userid='User_1';
```
