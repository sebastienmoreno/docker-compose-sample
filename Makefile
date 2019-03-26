build:
	docker build --tag provider python-provider
	docker build --tag client python-client

all: clean build launch

launch:
	-docker network create -d bridge python
	docker run --network python -d -p 8080:8080 --name provider provider
	docker run --network python -d --name client client

stop:
	-docker rm -f client provider

clean: stop
	-docker rmi -f client provider
	-docker network rm python