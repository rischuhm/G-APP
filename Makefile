.PHONY: docker

docker:
	docker build -t mapps:latest .

docker-run:
	docker run -p 80:80 -p 443:443 --name nginx -it --rm mapps:latest
