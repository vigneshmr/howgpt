export PYTHONPATH=$(shell pwd)/     

test:
	@python -m unittest discover -s _1_math -p "test_*.py"
