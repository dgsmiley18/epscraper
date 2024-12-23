from setuptools import setup
import configparser
config = configparser.ConfigParser()
config.read('setup.cfg')
metadata = config['metadata']

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=metadata['name'],
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['author_email'],
    description=metadata['description'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dgsmiley18/epscraper",
    packages=["epscraper"],
    license="GPLv3",
    entry_points={'console_scripts': ['epscraper=epscraper.__main__:main']},
    install_requires=[
        "beautifulsoup4",
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
