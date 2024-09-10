# Alation with EDF

## Alation installation

`curl -kLH "Authorization: Token d8823750607f64e4c9708fe3ab0aa94e3d5281e8" https://customerportal.alationdata.com/api/build_artifact/37507/download/ > alation-2024.3-19.0.0.85267.rpm`

<!-- ## Kerberos Server?

[Simple KDC](https://github.com/staticmukesh/kerberos-docker)

and/or

https://www.confluent.io/en-gb/blog/containerized-testing-with-kerberos-and-ssh/


Create user:
`kadmin.local -q "addprinc root/ezmeral@${REALM_NAME}"`

```bash
kinit root/ezmeral@${REALM_NAME}

ktutil
  - addent -password -p ezmeral@${REALM_NAME} -k 1 -e RC4-HMAC
  - wkt ezmeral.keytab
  - q
``` -->

## Alation installation

https://docs2.alationdata.com/en/latest/installconfig/ServerInstallation/Installation.html

## Catalog Sources

Add data source
Custom DB

For advanced settings, we might try:

https://docs.alationdata.com/en/latest/archive/AddDataSources/Hive/ConfigurationBasedHive.html#getting-hive-client-configuration-files


Add data source using following configuration:

Copy truststore to Alation host:

`scp mapr@vm25.kayalab.uk:/opt/mapr/conf/ssl_truststore /opt/alation/alation/data1`

Get truststore password from mapr:

`ssh mapr@vm25.kayalab.uk "grep ssl.server.truststore.password /opt/mapr/conf/store-passwords.txt | cut -d'=' -f2"`

JDBC URI:

`hive2://vm25.kayalab.uk:10000/default;ssl=true;user=mapr;password=mapr123;sslTrustStore=/data1/mapr_ssl_truststore;trustStorePassword=_niK5JPOy_yhxD74nq78QCbsKbVaOWEh`

Use 'hive' as service account.

Skip QLI

Metadata extraction

Data Sampling

Monitor from `/opt/alation/alation/data1/site_data/logs/taskserver.log`
