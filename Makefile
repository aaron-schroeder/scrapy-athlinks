init:
	pip install -r requirements_dev.txt
	pip install -r requirements.txt

test:
	python -m unittest tests
	# python -m unittest discover -s 'tests' -p 'test*.py' -v

# doc:
# 	make -C docs/ clean
# 	make -C docs/ html

clean:
	rm -Rf *.egg-info build dist

testpublish:
	# git push origin && git push --tags origin
	$(MAKE) clean
	# pip install --quiet twine wheel
	# pip install twine wheel
	# python setup.py bdist_wheel
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload -r testpypi dist/*
	# $(MAKE) clean

publish:
	$(MAKE) clean
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload dist/*
	# $(MAKE) clean