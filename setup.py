import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='django-footprints',
	version='0.1',
	packages=find_packages(),
	include_package_data=True,
	license='MIT License',
	description='A simple Django app to track page views.',
	long_description=README,
	url='http://www.bokasolutions.com/django-footprints',
	author='Wayne T. Boka',
	author_email='wayne@bokasolutions.com',
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Django',
		'Framework :: Django :: 1.10',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
)
