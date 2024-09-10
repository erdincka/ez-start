# Alation with EDF

## Catalog Sources

Add data source
Custom DB

For advanced settings, we might try:

https://docs.alationdata.com/en/latest/archive/AddDataSources/Hive/ConfigurationBasedHive.html#getting-hive-client-configuration-files


Add data source using following configuration:

Copy truststore to Alation host:

`scp mapr@hostname.fqdn:/opt/mapr/conf/ssl_truststore /opt/alation/alation/data1`

Get truststore password from mapr:

`ssh mapr@hostname.fqdn "grep ssl.server.truststore.password /opt/mapr/conf/store-passwords.txt | cut -d'=' -f2"`

JDBC URI:

`hive2://hostname:10000/default;ssl=true;user=mapr;password=xxx;sslTrustStore=/data1/mapr_ssl_truststore;trustStorePassword=xxxxxx`

Use 'hive' as service account.

Skip QLI

Metadata extraction

Data Sampling

Monitor from `/opt/alation/alation/data1/site_data/logs/taskserver.log`
