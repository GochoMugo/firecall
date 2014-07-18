dist:
	@cp README.md README.txt
	@python setup.py sdist upload
	@rm README.txt
	@echo 'Dist build and uploaded...'

html:
	@cp README.md ./..
	@git checkout gh-pages
	@mv ../README.md .
	@python generate_html.py
	@git add README.md index.html
	@git commit -m "Updating Documentation"
	@git checkout master
	@echo "Docs generated well..."

clean:
	@rm -r firebasin/*pyc firebasin/__pycache__
	@echo 'Cleaned...'
