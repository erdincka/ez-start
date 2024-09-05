# Get started with Ezmeral


## Data Fabric

Simplest way to test functionality would be to use examples on one of the Data Fabric nodes, or use the [Docker Compose](./docker-compose.yml) file in this repo to build your client. Adjust the settings in the compose `environment` section to reflect your cluster.

`docker compose up` should start and configure a client container using [PACC image](https://hub.docker.com/r/maprtech/pacc).

PRO TIP: Create your own PACC image using [mapr-setup.sh](https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/AdvancedInstallation/CreatingPACCImage.html) script or [extend the image](https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/AdvancedInstallation/CustomizingaMapRPACC.html) with a `Dockerfile` and use it as your client.

### Setting up Ecosystem Components

- [Using Spark submit](./docs/Spark.md)

- [Using Hive with Delta tables](./docs/HiveForDelta.md)

- [Configure Hive with MariaDB](./docs/MariaDB_withHive.md)

- [Configure Ranger](./docs/Ranger.md)

- [Configure Tez and Hive](./docs/TEZ_UI.md)

- [Using Zeppelin with Parquet and Hive](./docs/Zeppelin.md)


### Mock data

Got data set from kaggle.com: https://www.kaggle.com/datasets/gauravduttakiit/power-plant-data

- Power plant sensor data:

    Testing set:
    `AT,EV,AP,RH`

    Training set:
    `AT,EV,AP,RH,PE`


### Data ingestion

Batch and streaming ingestion.

- [Python OJAI for DocumentDB](./tables.py)

- [Python deltalake Tables](./delta.py)


## Files and Objects


Protocols: SFTP, HDFS, REST, NFS etc

- [NFS](./docs/NFSMount.md)

- HDFS:

    ```bash
    hadoop fs -put ./data/Testing_set_ccpp.csv
    hadoop fs -ls /
    ```

- [Python S3](./s3.py)

- [DocumentDB REST API](https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/MapR-DB/JSON_DB/GettingStartedMapRDBJSONRESTAPI.html)


### Streams

- [Using Spark Streaming](./docs/SparkStreamingDF.md)

- [Using KSQL](./docs/KSQL-demo.md)

- [Kafka Python](./streams.py)

- [Kafka REST API](https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/Kafka/REST-post-topic-partition-message.html)


### ETL & Data Processing

- Airflow

- NiFi


## Unified Analytics

### Exploratory analysis and cleaning

Attach data sources to UA.

Data Fabric: S3, Volumes
Presto: RDBMS, HDFS, Delta Lake, etc.

Jupyter Notebooks, Ray or Spark on UA.

- Pandas, Seaborn, Matplotlib, etc.

### Data distribution

Jupyter notebook

### Correlation analysis

Jupyter notebook

### Outliers detection

Jupyter notebook

### Missing values detection

Jupyter notebook

### Data preprocessing

Jupyter notebook - Spark / Ray

### Data visualization

Jupyter notebook & Superset

### Publish data in S3


## Model training

Jupyter notebook - Sklearn/XGB/Ray/PySpark/Pytorch/H2O/Tensorflow...

### Feature engineering

Jupyter notebook - Feast

### Model building

Jupyter notebook - Ray Train / Spark etc.

### Model evaluation

MLFlow, Kubeflow, Ray...

### Model selection

MLFlow, Whylogs

### Model registry

MLFlow

### Model distribution

Github, Data Fabric?

## Model serving

TensorRT, KServe, Ray Serve...


## References
