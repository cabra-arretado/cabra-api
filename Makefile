default: help

.PHONY: all clean

help: # Show help
	@grep -E '^[_/a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

# Database container
sql/docker_image: # Build docker image for MySQL server
	docker build -t cabra-sql:latest ./mysql

sql/run: # Run docker container for MySQL server
	docker run -p 3306:3306 cabra-sql:latest

sql/update_run: sql/docker_image sql/run # Update docker image and run MySQL container

######################

# FastAPI container
fastapi/docker_image: # Build docker image for FastAPI server
	docker build -t fastapi:latest ./fastapi

fastapi/run_docker: # Run docker container for FastAPI server
	docker run -d -p 8000:8000 fastapi:latest

fastapi/update_run: fastapi/docker_image fastapi/run_docker # Update docker image and run FastAPI container

fastapi/run: # Run FastAPI server without container
	cd fastapi && pipenv run uvicorn main:app --reload

######################

# Update all images and run docker-compose
run: sql/docker_image fastapi/docker_image # Update all images and run docker-compose
	docker-compose up -d
