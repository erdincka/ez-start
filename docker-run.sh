#!/usr/bin/env bash

cd /

[ -z "$( ls -A '/app' )" ] || git clone https://github.com/erdincka/pacc-app.git

cd /app

# connect and configure if not configured already
# [ -z "$( ls -A '/mapr' )" ] || bash -c ./connect_and_configure.sh
[ -z "$( ls /tmp/maprticket_${MAPR_CONTAINER_UID} )" ] || bash -c ./connect_and_configure.sh

sleep infinity
