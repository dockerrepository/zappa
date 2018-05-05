build_python27:
	docker build -f python-2.7/Dockerfile -t nsantana/zappa-docker:2.7 ./python-2.7/

build_python36:
	docker build -f python-3.6/Dockerfile -t nsantana/zappa-docker:3.6 ./python-3.6/