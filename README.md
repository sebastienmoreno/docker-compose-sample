# Python Docker container to test client/server and scalability

# By hand

## build
docker build --tag provider python-provider
docker build --tag client python-client

## run
docker rm -f provider client
docker network create -d bridge python
docker run --network python -d -p 8080:8080 --name provider provider
docker run --network python -d --name client client

# By Makefile

## Build
make

## Launch
make launch

## Clean all
make clean

# By compose

Build first with 'make' then execute by compose:

# Launch
docker-compose up -d

# Scale
docker-compose up --scale provider=5 -d

# Clean
docker-compose down
make clean