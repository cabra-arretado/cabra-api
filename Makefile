.PHONY: all clean

all: requirements

requirements:
	pipenv requirements > requirements.txt
	pipenv requirements --dev > requirements-dev.txt

clean:
	rm -f requirements.txt requirements-dev.txt

docker_image:
	docker build -t fastapi:latest .

run_docker:
	docker run -d -p 8000:8000 fastapi:latest
