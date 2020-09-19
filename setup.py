from setuptools import setup, find_packages


NAME = 'profile-readme'
VERSION = '0.1.0'
DESCRIPTION = ''
URL = ''
EMAIL = ''
AUTHOR = ''
REQUIRES_PYTHON = '>=3.4.0'
LICENSE = 'MIT'

PROJECT_URLS = {
    "Bug Tracker": "",
    "Documentation": "",
    "Source": ""
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
        profile-readme=src.cli:cli
    ''',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",

        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",

        "Environment :: Console",

        "Programming Language :: Cython",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

        "Operating System :: OS Independent",

        "Topic :: Software Development :: Libraries",
    ],
    keywords="profile-readme",
)
