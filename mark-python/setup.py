# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mark',
 'mark.compiler',
 'mark.compiler.classes',
 'mark.compiler.lang',
 'mark.compiler.parser',
 'mark.compiler.require',
 'mark.config',
 'mark.dev',
 'mark.utils']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.3.6,<4.0.0',
 'htmlmin>=0.1.12,<0.2.0',
 'lesscpy>=0.15.0,<0.16.0',
 'libsass>=0.21.0,<0.22.0',
 'livereload>=2.6.3,<3.0.0',
 'pyinotify>=0.9.6,<0.10.0',
 'rcssmin>=1.1.0,<2.0.0',
 'rjsmin>=1.2.0,<2.0.0',
 'six>=1.16.0,<2.0.0',
 'termcolor>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'mark',
    'version': '0.0.0',
    'description': 'Never write a single line of HTML anymore! A modern markup language for the 21st century',
    'long_description': None,
    'author': 'baris-inandi',
    'author_email': '68742481+baris-inandi@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/baris-inandi/mark',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
