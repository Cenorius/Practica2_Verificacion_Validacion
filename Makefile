init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	coverage run practica/data_base.py
	coverage report -m --omit=ENV/*
