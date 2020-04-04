try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


config = {
	'description': 'Парсер и поисковая выдача ',
	'author': 'xaldey',
	'url': 'https://github.com/xaldey/parserSerp',
	'download_url': 'https://github.com/xaldey/parserSerp',
	'author_email': 'Мой email',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['Parse'],		
	'scripts': [],
	'name': 'parserSerp',	
}

setup(**config)