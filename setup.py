from setuptools import setup, find_packages
import os

version = '0.4.dev0'


def read(*rnames):
    """Read in file content."""
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


long_description = (
    read('README.rst')
    + '\n' +
    read('CHANGES.rst'))


setup(
    name='js.tableselect',
    version=version,
    description="Fanstatic package providing a js table select widget.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Daniel Havlik',
    author_email='dh@gocept.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery',
        'js.jquery_datatables',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'namespace = js.tableselect:library',
        ],
    },
)
