.PHONY: dist clean

dist:
	@cp README.md README.txt
	@python setup.py sdist upload
	@rm README.txt
	@echo 'Dist build and uploaded...'

clean:
	@rm -rf firecall/*pyc firecall/__pycache__ build dist
	@echo 'Cleaned...'
