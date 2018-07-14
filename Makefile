
clean:
	rm -rf *.egg-info
	rm -rf dist/
	rm -rf build/

init:
	bash ./bin/init.sh

test:
	python -m pytest tests

package:
	python setup.py sdist bdist_wheel

distribute:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: clean distribute init test package
