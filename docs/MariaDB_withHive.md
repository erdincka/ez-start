# Using MariaDB with Hive

## Install MariaDB (if not already installed)

Follow the documentation for MariaDB for your platform (Rocky, RHEL, Ubuntu etc).

The following commands assume that you are running your Data Fabric on RHEL-based Linux environment (Rocky, Centos, RHEL etc). Refer to your OS package manager for other options (ie, Ubuntu).

## Install Hive metastore

Install hive and hive metastore

`yum install mapr-hive mapr-hiveserver2 mapr-hivemetastore`

### Download MariaDB packages:

<!-- Not sure why Hive uses 2.5.4 version and NiFi below uses 3.4.1 version -->
`wget https://downloads.mariadb.com/Connectors/java/connector-java-2.5.4/mariadb-java-client-2.5.4.jar`
`wget https://downloads.mariadb.com/Connectors/java/connector-java-2.5.4/mariadb-java-client-2.5.4-sources.jar`
`wget https://downloads.mariadb.com/Connectors/java/connector-java-2.5.4/mariadb-java-client-2.5.4-javadoc.jar`

Copy files to /opt/mapr/hive/hive-3.1.3/lib/

Install MariaDB connector for NiFi
`wget https://dlm.mariadb.com/3852266/Connectors/java/connector-java-3.4.1/mariadb-java-client-3.4.1.jar -O /mapr/fraud/user/root/mariadb-java-client-3.4.1.jar`


### Initialize Hive database

Reconfigure cluster:

`/opt/mapr/server/configure.sh -R`

Follow the doc to set up database: https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/Hive/Config-MariaDBForHiveMetastore.html


Edit `/opt/mapr/hive/hive-3.1.3/conf/hive-site.xml`

Initialize: `/opt/mapr/hive/hive-3.1.3/bin/schematool -dbType mysql -initSchema`


## Create Dashboard DBs

```shell

mysql -u root -p

CREATE DATABASE mydb;

CREATE USER 'CHANGEME'@'%' IDENTIFIED BY 'CHANGEME';

GRANT ALL ON mydb.* TO 'CHANGEME'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

exit

```
