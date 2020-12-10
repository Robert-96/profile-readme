from setuptools import setup, find_packages


NAME = 'profile-readme'
VERSION = '0.1.2'
DESCRIPTION = 'A CLI tool for generating a GitHub profile README using the Jinja2 template engine.'
URL = 'https://github.com/Robert-96/profile-readme'
EMAIL = 'dezmereanrobert@gmail.com'
AUTHOR = 'Robert-96'
REQUIRES_PYTHON = '>=3.4.0'
LICENSE = 'MIT'

PROJECT_URLS = {
    'Bug Tracker': 'https://github.com/Robert-96/profile-readme/issues/',
    'Documentation': 'https://profile-readme.rtfd.io/',
    'Source': 'https://github.com/Robert-96/profile-readme/'
}

with open('requirements.txt') as f:
    REQUIRED = f.read().splitlines()

with open('README.md') as f:
    README = f.read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    license=LICENSE,
    url=URL,
    project_urls=PROJECT_URLS,

    author=AUTHOR,
    author_email=EMAIL,

    python_requires=REQUIRES_PYTHON,
    setup_requires=REQUIRED,
    install_requires=REQUIRED,
    packages=find_packages(exclude=['tests']),
    entry_points='''
        [console_scripts]
        profile-readme=profile_readme.cli:cli
    ''',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',

        'Environment :: Console',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Cython',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

        'Operating System :: OS Independent',

        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: Markdown',
        'Topic :: Utilities'
    ],
    keywords='profile-readme, github, profile, readme',
)
