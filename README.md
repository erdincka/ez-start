# Get started with Ezmeral Data Fabric

Copy the code you wish to try on one of the Data Fabric nodes, or use the [Docker Compose](./docker-compose.yml) file in this repo to build your client. Adjust the settings in the compose to reflect your cluster.

## Clone the repository

`git clone https://github.com/erdincka/pacc-app.git`

## Mocked data

Got 2 data sets from kaggle.com.
<!-- add reference/url for the data sets -->

- Energy production and weather data from 2 different solar power plants:

    Production data:
    `DATE_TIME,PLANT_ID,SOURCE_KEY,DC_POWER,AC_POWER,DAILY_YIELD,TOTAL_YIELD`

    Weather data:
    `DATE_TIME,PLANT_ID,SOURCE_KEY,AMBIENT_TEMPERATURE,MODULE_TEMPERATURE,IRRADIATION`

- Power plant sensor data:

    Testing set:
    `AT,EV,AP,RH`

    Training set:
    `AT,EV,AP,RH,PE`


## Data ingestion

S3 and Kafka are used to ingest data.

Airflow / NiFi

### Files & Objects

SFTP, HDFS, REST, etc.

- Read csv

- Write to S3 bucket


### Streams

- Read csv

- Write to topic


## Exploratory analysis and cleaning

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
