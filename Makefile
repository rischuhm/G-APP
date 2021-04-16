docker:
	docker build -t mapps:latest .

docker-run:
	docker run -p 8000:8000 -it --rm mapps:latest