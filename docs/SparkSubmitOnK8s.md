#!/usr/bin/env bash

`export SPARK_HOME=/opt/mapr/spark/spark-3.5.1`

```bash

/opt/mapr/spark/spark-3.5.1/bin/spark-submit \
    --master k8s://https://CHANGEME:443 \
    --deploy-mode cluster \
    --conf spark.kubernetes.namespace=CHANGEME \
    --conf spark.app.name=test1a \
    --conf spark.kubernetes.driver.pod.name=test1a-driver \
    --conf spark.kubernetes.container.image=gcr.io/mapr-252711/spark-py-3.5.1:v3.5.1.0.1 \
    --conf spark.kubernetes.container.image.pullPolicy=Always \
    --conf spark.kubernetes.container.image.pullSecrets=imagepull \
    --conf spark.kubernetes.submission.waitAppCompletion=false \
    --conf spark.executorEnv.SPARK_USER=CHANGEME \
    --conf spark.kubernetes.driverEnv.SPARK_USER=CHANGEME \
    --conf spark.mapr.user.secret=hpe-autotix-generated-secret-CHANGEME \
    --conf spark.mapr.user.secret.autogen=true \
    --conf spark.kubernetes.driver.label.sparkoperator.hpe.com/app-name=test1a \
    --conf spark.kubernetes.driver.label.sparkoperator.hpe.com/launched-by-spark-operator=true \
    --conf spark.kubernetes.driver.label.sparkoperator.hpe.com/submission-id=CHANGEME \
    --conf spark.driver.cores=1 \
    --conf spark.kubernetes.driver.limit.cores=1 \
    --conf spark.driver.memory=1G \
    --conf spark.kubernetes.authenticate.driver.serviceAccountName=hpe-CHANGEME \
    --conf spark.kubernetes.driver.label.hpe-ezua/type=app-service-user \
    --conf spark.kubernetes.driver.label.sidecar.istio.io/inject=false \
    --conf spark.kubernetes.driver.label.hpe-ezua/app=spark \
    --conf spark.kubernetes.driver.label.version=3.5.1 \
    --conf spark.kubernetes.executor.label.sparkoperator.hpe.com/app-name=test1a \
    --conf spark.kubernetes.executor.label.sparkoperator.hpe.com/launched-by-spark-operator=true \
    --conf spark.kubernetes.executor.label.sparkoperator.hpe.com/submission-id=CHANGEME \
    --conf spark.executor.instances=1 \
    --conf spark.executor.cores=1 \
    --conf spark.kubernetes.executor.limit.cores=1 \
    --conf spark.executor.memory=1G \
    --conf spark.kubernetes.executor.label.version=3.5.1 \
    --conf spark.kubernetes.executor.label.hpe-ezua/type=app-service-user \
    --conf spark.kubernetes.executor.label.sidecar.istio.io/inject=false \
    --conf spark.kubernetes.executor.label.hpe-ezua/app=spark local:///mounts/shared-volume/user/sparker.py

```