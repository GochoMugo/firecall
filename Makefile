.PHONY: dist clean

dist:
	@cp README.md README.txt
	@python setup.py sdist upload
	@rm README.txt
	@echo 'Dist build and uploaded...'

clean:
	@rm -rf firebasin/*pyc firebasin/__pycache__ build dist
	@echo 'Cleaned...'
