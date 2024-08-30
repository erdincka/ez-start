#!/usr/bin/env bash

set -euo pipefail

# Setup the pacc instance
apt update
apt upgrade -y
apt install -y locales openssh-client sshpass python3-pip
locale-gen en_US.UTF-8
pip3 install --global-option=build_ext --global-option="--library-dirs=/opt/mapr/lib" --global-option="--include-dirs=/opt/mapr/include/" mapr-streams-python
pip3 install maprdb-python-client deltalake pandas

# Setup SSH
[ -f /root/.ssh/id_rsa ] || ssh-keygen -t rsa -b 2048 -f /root/.ssh/id_rsa -q -N ""

# remove old entries
ssh-keygen -f "/root/.ssh/known_hosts" -R ${MAPR_CLDB_HOSTS} || true # ignore errors/not-found
sshpass -p "${MAPR_CONTAINER_PASSWORD}" ssh-copy-id -o StrictHostKeyChecking=no "${MAPR_CONTAINER_USER}@${MAPR_CLDB_HOSTS}"

scp -o StrictHostKeyChecking=no ${MAPR_CONTAINER_USER}@$MAPR_CLDB_HOSTS:/opt/mapr/conf/ssl_truststore* /opt/mapr/conf/

# This is already done by the pacc image
# /opt/mapr/server/configure.sh -c -secure -N ${MAPR_CLUSTER} -C ${MAPR_CLDB_HOSTS}
# echo "Finished configuring MapR"

scp -o StrictHostKeyChecking=no ${MAPR_CONTAINER_USER}@$MAPR_CLDB_HOSTS:/opt/mapr/conf/maprkeycreds* /opt/mapr/conf/
scp -o StrictHostKeyChecking=no ${MAPR_CONTAINER_USER}@$MAPR_CLDB_HOSTS:/opt/mapr/conf/maprtrustcreds* /opt/mapr/conf/
scp -o StrictHostKeyChecking=no ${MAPR_CONTAINER_USER}@$MAPR_CLDB_HOSTS:/opt/mapr/conf/maprhsm.conf /opt/mapr/conf/

### Update ssl conf
if grep hadoop.security.credential.provider.path /opt/mapr/conf/ssl-server.xml ; then
  echo "Skip /opt/mapr/conf/ssl-server.xml"

else
  echo "Adding property to /opt/mapr/conf/ssl-server.xml"

  grep -v "</configuration>" /opt/mapr/conf/ssl-server.xml > /tmp/ssl-server.xml

  echo """
<property>
  <name>hadoop.security.credential.provider.path</name>
  <value>localjceks://file/opt/mapr/conf/maprkeycreds.jceks,localjceks://file/opt/mapr/conf/maprtrustcreds.jceks</value>
  <description>File-based key and trust store credential provider.</description>
</property>

</configuration>
""" >> /tmp/ssl-server.xml

  mv /tmp/ssl-server.xml /opt/mapr/conf/ssl-server.xml

fi

# create user ticket
echo ${MAPR_CONTAINER_PASSWORD} | maprlogin password -user ${MAPR_CONTAINER_USER}

# Mount /mapr
([ -d /mapr ] && umount -l /mapr) || mkdir /mapr

mount -t nfs4 -o nolock,soft ${MAPR_CLDB_HOSTS}:/mapr /mapr

echo "Client is ready"
