.PHONY: all clean

sql/docker_image:
	docker build -t cabra-sql:latest ./mysql
