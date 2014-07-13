dist:
	@cp README.md README.txt
	@python setup.py sdist upload
	@rm README.txt
	@echo 'Dist build and uploaded...'

clean:
	@rm -r firebasin/*pyc firebasin/__pycache__
	@echo 'Cleaned...'
