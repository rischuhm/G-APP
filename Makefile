.PHONY: docker

docker:
	docker build -t mapps:latest .

docker-run:
	docker run -p 80:80 -it --rm mapps:latest
