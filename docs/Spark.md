# Using Spark

Following up from:
https://spark.apache.org/docs/latest/submitting-applications.html

Integrate Spark with EEP components

https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/Spark/IntegrateSpark.html


## Spark Submit

**spark-submit will fail if run as root when using yarn mode**
https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/Spark/UseSparkonYARN.html


```bash

su - mapr

export SPARK_VERSION=3.5.1
export SPARK_HOME="/opt/mapr/spark/spark-${SPARK_VERSION}"

# copy the jar to the cluster

cp $SPARK_HOME/examples/jars/*.jar /mapr/CHANGEME/apps/

# using file:/// uri
$SPARK_HOME/bin/spark-submit --deploy-mode cluster \
    --class org.apache.spark.examples.SparkPi \
    --master yarn \
    --deploy-mode cluster \
    file:///mapr/CHANGEME/apps/spark-examples_2.12-${SPARK_VERSION}.0-eep-930.jar 10

# alternatively using maprfs:/// uri
$SPARK_HOME/bin/spark-submit --deploy-mode cluster \
    --class org.apache.spark.examples.SparkPi \
    --master yarn \
    --deploy-mode cluster \
    maprfs:///apps/spark-examples_2.12-${SPARK_VERSION}.0-eep-930.jar 10

```

Get logs/results from History Server or yarn logs
