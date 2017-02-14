from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

VERSION = (0, 1, 0)

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='addok-pg',
    version=".".join(map(str, VERSION)),
    description="Store documents in postgresql.",
    long_description=long_description,
    url='https://github.com/addok/addok-pg',
    author='Christian Quest',
    author_email='christian.quest@data.gouv.fr',
    license='WTFPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: GIS',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='addok geocoding postgresql',
    packages=find_packages(exclude=['tests']),
    extras_require={'test': ['pytest']},
    include_package_data=True,
    entry_points={'addok.ext': ['postgresql=addok_pg.plugin']},
)
