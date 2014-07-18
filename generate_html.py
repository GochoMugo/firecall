'''
Generates HTML Using the README and template in the Directory
'''

import os
import re


def read_file(path):
    with open(path, 'r') as content:
        return content.read()


def write_file(path, content):
    with open(path, 'w') as my_file:
        my_file.write(content)


def generate_html():
    template = read_file('template.html')
    readme = read_file('README.md')
    version = re.search(r'Version.*(\d.\d.\d)', readme).group(1)
    status = re.search(r'Status[.\|\s]*(\w.*\w)[\s\|]*', readme).group(1)
    last_updated = re.search(r'Updated[.\|\s]*(\w.*\w)[\s\|]*', readme).group(1)
    new_content = readme[readme.index("## Prerequisites"):]
    template = template.format(
        version=version,
        status=status,
        last_updated=last_updated,
        content=new_content
    )
    write_file('index.html', template)

if __name__ == '__main__':
    generate_html()
