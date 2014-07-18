'''
Generates HTML Using the markdown files and templates in the Directory
'''

import os
import re


def read_file(path):
    with open(path, 'r') as content:
        return content.read()


def write_file(path, content):
    with open(path, 'w') as my_file:
        my_file.write(content)


def generate_html(template, markdown, html, formatting):
    template = read_file(template)
    raw = read_file(markdown)
    template = formatting(template, raw)
    write_file(html, template)

def index(template, markdown):
    version = re.search(r'Version.*(\d.\d.\d)', markdown).group(1)
    status = re.search(r'Status[.\|\s]*(\w.*\w)[\s\|]*', markdown).group(1)
    last_updated = re.search(r'Updated[.\|\s]*(\w.*\w)[\s\|]*', markdown).group(1)
    new_content = markdown[markdown.index("## Prerequisites"):]
    template = template.format(
        version=version,
        status=status,
        last_updated=last_updated,
        content=new_content
    )
    return template

if __name__ == '__main__':
    generate_html('templates/index.html', 'docs/index.md', 'index.html', index)
    # generate_html('templates/changes.html', 'docs/changes.md', 'changes.html')
