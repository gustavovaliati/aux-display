run:
	docker build -t aux-display-server .
	docker run -it -p 8081:8081 aux-display-server