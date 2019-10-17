[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b4cc57784e324eb5b1ebb8d68478277b)](https://app.codacy.com/app/ZoranPandovski/GIC?utm_source=github.com&utm_medium=referral&utm_content=AAYBS/GIC&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/AAYBS/GIC.svg?branch=master)](https://travis-ci.org/AAYBS/GIC)
[![BCH compliance](https://bettercodehub.com/edge/badge/AAYBS/GIC?branch=master)](https://bettercodehub.com/)
[![Known Vulnerabilities](https://snyk.io/test/github/AAYBS/GIC/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/AAYBS/GIC?targetFile=requirements.txt)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/AAYBS/GIC.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/AAYBS/GIC/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/AAYBS/GIC.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/AAYBS/GIC/context:python)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/ZoranPandovski/al-go-rithms/issues)

# GitHub Issue Creator
This project automates the creation of repetitive tasks, as creating GitHub issues to get more contributors. 
GitHub provides API action for most of the stuff that you can do through UI, check out [GitHub API](https://developer.github.com/v3/), but this project was created for fun to practice Selenium and POM design pattern. Page Object Model is used as a design pattern which has become popular in test automation for enhancing test maintenance and reducing code duplication. More information about [Selenium](https://able.bio/ZoranPandovski/introduction-to-selenium--75njv2f) or Page Object Models: [PageObjects](https://github.com/SeleniumHQ/selenium/wiki/PageObjects)

## Installation
```
pip install -r requirements.txt
```

## Config Settings
Basic configuration options:
```
# Login page configuration
[LOGIN]
USER_NAME=your_username
PASSWORD=your_password

# Issue page configuration
[ISSUES]
TITLE=Issue title
DESCRIPTION=Issue description!
# Comma separated list of already created label names
LABELS=documentation,bug

# Browser configuration
[BROWSER]
# One of CHROME, FIREFOX
USE_BROWSER=CHROME

# URL configuration
[URL]
# The starting page for the browser driver, can just be the same as DEFAULT_URL
START_PAGE_URL = https://github.com/thockin/test/issues
# The URL of the issues page of the repo which the tool will create an issue on
DEFAULT_URL = https://github.com/thockin/test/issues
```

## Running project
```
python creator.py
```
