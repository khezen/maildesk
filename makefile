tools:
	python3 -m pip install --user --upgrade setuptools wheel twine
dist:
	python3 setup.py sdist bdist_wheel
publish:
	python3 -m twine upload dist/*
