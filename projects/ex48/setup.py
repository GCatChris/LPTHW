try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup
	
config = {
	'description': 'My Project',
	'author': 'Chris Khoury',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'gcatchris@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)