#! /bin/bash

WORKDIR='/tmp/lambda/zip/'

cd aws/lambda/src
for dir in `ls -d */`
do
    zip ${WORKDIR}`basename ${dir}`.zip `basename ${dir}`
done

aws s3 sync --exact-timestamps --delete ${WORKDIR} s3://quark-cicd-test/lambda/src/