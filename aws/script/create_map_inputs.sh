#! /bin/bash

TARGET_FILE='aws/stepfunctions/distributed-map-source.csv'
echo "bucket,file_key" >> ${TARGET_FILE}
for f in `ls aws/s3/create_table_query | grep .sql`
do
    echo "quark-cicd-test,s3/create_table_query/${f}" >> ${TARGET_FILE}
done

aws s3 cp ${TARGET_FILE} s3://quark-cicd-test/stepfunctions/distributed-map-source.csv