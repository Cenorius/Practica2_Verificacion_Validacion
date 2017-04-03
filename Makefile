init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	coverage run practica/practica.py
	coverage report -m
