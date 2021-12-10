#!/bin/bash

if [ "$1" == "deploy" ]; then
	aws cloudformation deploy --template-file aws_cfn.yml --stack-name mlog --capabilities CAPABILITY_IAM
elif [ "$1" == "delete" ]; then
	aws cloudformation delete-stack --stack-name mlog
else
	>&2 echo "Please select option from 'deploy' or 'delete'"
	false
fi
