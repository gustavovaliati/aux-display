run:
	docker build -t aux-display-server .
	docker run -it -p 8080:8080 aux-display-server