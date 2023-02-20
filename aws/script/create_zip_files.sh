#! /bin/bash

WORKDIR='/tmp/lambda/zip/'
mkdir -p ${WORKDIR}

cd aws/lambda/src
for dir in `ls -d */`
do
    zip -r -j ${WORKDIR}`basename ${dir}`.zip `ls ${dir}/* | grep lambda_function.py`
done

aws s3 sync --exact-timestamps --delete ${WORKDIR} s3://quark-cicd-test/lambda/src/