.PHONY: install run test build docker-build clean

install:
	pip install -r requirements.txt

run:
	python main.py

test:
	pytest --cov=app tests/

build:
	python -m compileall app/

docker-build:
	docker build -t trippilot-saas .

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
