# Tez And Hive integration

First install ATSv1

## Configure ATS for v1.5

https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/MapROverview/c_configuring_ATS_for_yarn.html

### On all nodes, edit and add following xml section in
/opt/mapr/hadoop/hadoop-3.3.5/etc/hadoop/yarn-site.xml

```xml
  <property>
      <name>yarn.timeline-service.enabled</name>
      <value>true</value>
  </property>
  <property>
      <name>yarn.timeline-service.hostname</name>
      <value>CHANGEME</value>
  </property>
  <property>
      <name>yarn.resourcemanager.system-metrics-publisher.enabled</name>
      <value>true</value>
  </property>
  <property>
      <name>yarn.timeline-service.http-cross-origin.enabled</name>
      <value>true</value>
  </property>
   <property>
      <name>yarn.timeline-service.version</name>
      <value>1.5f</value>
      <description>Timeline server version. Should be 1.0f or 1.5f</description>
  </property>
  <property>
      <name>yarn.timeline-service.entity-group-fs-store.summary-store</name>
      <value>org.apache.hadoop.yarn.server.timeline.RollingLevelDBTimelineStore</value>
  </property>
  <property>
      <name>yarn.timeline-service.store-class</name>
      <value>org.apache.hadoop.yarn.server.timeline.EntityGroupFSTimelineStore</value>
  </property>
  <property>
      <name>yarn.timeline-service.entity-group-fs-store.active-dir</name>
      <value>/apps/ats/active/</value>
  </property>
  <property>
      <name>yarn.timeline-service.entity-group-fs-store.done-dir</name>
      <value>/apps/ats/done/</value>
  </property>
  <property>
      <name>yarn.timeline-service.leveldb-timeline-store.path</name>
      <value>/opt/mapr/hadoop/hadoop-3.3.5/ats/leveldb/</value>
  </property>
  <property>
      <name>yarn.timeline-service.entity-group-fs-store.group-id-plugin-classes</name>
      <value>org.apache.tez.dag.history.logging.ats.TimelineCachePluginImpl</value>
  </property>
  <property>
    <name>yarn.timeline-service.http-authentication.type</name>
    <value>org.apache.hadoop.security.token.delegation.web.MaprDelegationTokenAuthenticationHandler</value>
  </property>
```

### Commands to configure ATSv1.5

```bash

# On the node it is installed
dnf remove -y mapr-timelineserver

# On one node
hadoop fs -mkdir -p /apps/ats/active/
hadoop fs -mkdir -p /apps/ats/done/
hadoop fs -chmod 1777 /apps/ats/active/
hadoop fs -chmod 0700 /apps/ats/done/

mkdir -p /opt/mapr/hadoop/hadoop-3.3.5/ats/leveldb/
chown -R mapr:root /opt/mapr/hadoop/hadoop-3.3.5/ats

cp /opt/mapr/tez/tez-0.10.2/tez-yarn-timeline-cache-plugin-0.10.2.400-eep-921.jar /opt/mapr/hadoop/hadoop-3.3.5/share/hadoop/yarn/lib/
cp /opt/mapr/tez/tez-0.10.2/tez-api-0.10.2.400-eep-921.jar /opt/mapr/hadoop/hadoop-3.3.5/share/hadoop/yarn/lib/
cp /opt/mapr/tez/tez-0.10.2/tez-common-0.10.2.400-eep-921.jar /opt/mapr/hadoop/hadoop-3.3.5/share/hadoop/yarn/lib/

# on all nodes
maprcli node services -nodes `hostname -f` -name resourcemanager -action restart
maprcli node services -nodes `hostname -f` -name nodemanager -action restart
maprcli node services -nodes `hostname -f` -name historyserver -action restart

# on ATS node
dnf install -y mapr-timelineserverv1

# on all nodes
/opt/mapr/server/configure.sh -R -TL CHANGEME

# on ATS node
maprcli node services -nodes `hostname -f` -name timelineserverv1 -action start


```

### Edit service URL for timelineserver1

In /opt/mapr/conf/conf.d/warden.timelineserverv1.conf

service.ui.port=8190

## Follow the Doc for Tez UI

https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/Hive/Hive_and_Tez_Config.html


### Add Tez UI URL to tez-site.xml

```xml
    <property>
        <description>Enable Tez to use the Timeline Server for History Logging</description>
        <name>tez.history.logging.service.class</name>
        <value>org.apache.tez.dag.history.logging.ats.ATSHistoryLoggingService</value>
    </property>
    <property>
     <description>URL for where the Tez UI is hosted</description>
        <name>tez.tez-ui.history-url.base</name>
        <value>https://<hostname>:<port>/tez-ui/</value>
    </property>
```

## Fix UI links
cp /opt/mapr/tez/tez-0.10.2/conf/warden.tezui.conf.template /opt/mapr/tez/tez-0.10.2/conf/warden.tezui.conf

### Edit
/opt/mapr/conf/conf.d/warden.tezui.conf

#### Replace
service.ui.port=9393
service.uri=/tez-ui

## MONITOR TEZ UI
/opt/mapr/tez/tez-0.10.2/tomcat/apache-tomcat-9.0.76/logs/
