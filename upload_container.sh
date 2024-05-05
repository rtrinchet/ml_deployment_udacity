#!/usr/bin/env bash

account="230904673089"


echo "deploying to account $account"

export PATH="$PATH"
export branch=$(git symbolic-ref --short HEAD)
if [ -z "${branch}" ] ;
then
  echo 'We are in github workflow pull request triggered event read in the variable branch' ;
  export branch=${GITHUB_HEAD_REF}
fi
echo "the git branch is ${branch}"

ecr_repository="test"
processing_repository_uri="${account}.dkr.ecr.us-east-1.amazonaws.com/${ecr_repository}:cpu_${branch}"
docker_file_location="Dockerfile"

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${account}.dkr.ecr.us-east-1.amazonaws.com
docker build --no-cache -f $docker_file_location -t $ecr_repository . | tee image.build.log
docker tag $ecr_repository $processing_repository_uri
docker push $processing_repository_uri


