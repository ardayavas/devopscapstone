#!/usr/bin/env bash

CMD1="aws cloudformation update-stack \
--stack-name $1 \
--capabilities CAPABILITY_IAM 
--template-body file://$2 \
--parameters file://$3 \
--region=us-west-2"

$CMD1
