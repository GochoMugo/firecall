html: docs templates
	@python generate_html.py
	@git add *html
	@git commit -m "Updating Documentation"
	@echo "Docs generated well..."

