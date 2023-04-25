# Anime Episode Name Scraper

![GitHub stars](https://img.shields.io/github/stars/dgsmiley18/EpCrawler.svg?style=social&label=Star&maxAge=2592000)
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)

## **epcrawler** - get episode names from anidb

## 🎨 Table of Contents

- [Anime Episode Name Scraper](#anime-episode-name-scraper)
  - [**epcrawler** - get episode names from anidb](#epcrawler---get-episode-names-from-anidb)
  - [🎨 Table of Contents](#-table-of-contents)
  - [💾 Installation](#-installation)
  - [📙 Usage](#-usage)
  - [🖥️ Command line interface](#️-command-line-interface)

## 💾 Installation

To install Epcrawler, simply use `git clone https://github.com/dgsmiley18/EpCrawler.git`:


Check the [command line](%EF%B8%8F-command-line-interface) section for supported commands.

## 📙 Usage

Copy the name of the anime and pass it to `epcrawler`.

You can use `--name` and `--output` command line argument to specify the anime name and output file respectively.


## 🖥️ Command line interface

Currently `epcrawler` supports these commands

```bash
usage: Episode Finder [-h] -n NAME [-o OUTPUT]

Find the episodes names from your favorite anime!

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  specify the anime name
  -o OUTPUT, --output OUTPUT
                        specify the output file
```