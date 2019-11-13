#!/usr/bin/env bash

CMD1="aws cloudformation delete-stack \
--stack-name $1"

$CMD1