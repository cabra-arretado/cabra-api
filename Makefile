include fastapi/Makefile

.PHONY: all clean

# Database container
sql/docker_image:
	docker build -t cabra-sql:latest ./mysql

sql/run:
	docker run cabra-sql:latest

sql/update_run: sql/docker_image sql/run

######################

# FastAPI container
fastapi/docker_image:
	docker build -t fastapi:latest ./fastapi

fastapi/run_docker:
	docker run -d -p 8000:8000 fastapi:latest

fastapi/update_run: fastapi/docker_image fastapi/run_docker

fastapi/run:
	cd fastapi && pipenv run uvicorn fastapi.main:app --reload

######################

# Update all images and run docker-compose
run: sql/docker_image fastapi/docker_image
	docker-compose up -d
