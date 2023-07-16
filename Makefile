.PHONY: all clean

all: requirements

requirements:
	pipenv requirements > requirements.txt
	pipenv requirements --dev > requirements-dev.txt

clean:
	rm -f requirements.txt requirements-dev.txt
