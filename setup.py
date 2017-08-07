"""
Automatically send notifications at the end of a long running task
"""
from setuptools import find_packages, setup
from codecs import open
from os import path
import herald
from pypandoc import convert

dependencies = []


def read_md(f): return convert(f, 'rst')


setup(
    name='herald',
    version=herald.__version__,
    url='https://github.com/varunagrawal/nuke',
    license=herald.__license__,
    author=herald.__author__,
    author_email=herald.__email__,
    description='Command line tool to nuke a directory',
    long_description=read_md("README.md"),
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)