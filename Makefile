.PHONY: init run test build clean

init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Running Flask app locally..."
	python3 app.py

test:
	@echo "Running tests..."
	python3 test.py

build:
	@echo "Building Docker image..."
	docker build -t health-calculator .

clean:
	@echo "Cleaning Docker containers and images..."
	docker rm -f $$(docker ps -aq) || true
	docker rmi -f $$(docker images -q) || true
