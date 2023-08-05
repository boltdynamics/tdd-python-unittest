SHELL = /bin/bash
SHELLFLAGS = -ex

check-prerequisites: ## Check if all prerequisites are installed
	@echo "-- $(shell python --version)"
	@echo "-- $(shell pipenv --version)"

install-packages: ## Install dependencies
	pipenv install nose2 nose2-cov --dev
	@echo ""
	pipenv graph

test: ## Run Python unit tests from src/tests/ directory
	$(info [+] Running Python unit tests...)
	pipenv run nose2 --verbose tests

test-with-coverage: ## Run Python unit tests with coverage
	$(info [+] Running Python unit tests with coverage...)
	pipenv install nose2[coverage_plugin] --dev
	pipenv run nose2 --with-cov --coverage-report term-missing --coverage src tests

clean-environment: ## Clean environment - run with caution!!!!!
	-pipenv --rm
	rm -rf Pipfile*
	rm -rf htmlcov src tests .coverage
