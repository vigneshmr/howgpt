export PYTHONPATH=$(shell pwd)/     

test:
	@python -m unittest discover -s _1_math -p "test_*.py"

env:
	python3 -m venv env

run:
	env/bin/python 1_token/token.py
