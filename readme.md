[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b4cc57784e324eb5b1ebb8d68478277b)](https://app.codacy.com/app/ZoranPandovski/GIC?utm_source=github.com&utm_medium=referral&utm_content=AAYBS/GIC&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/AAYBS/GIC.svg?branch=master)](https://travis-ci.org/AAYBS/GIC)
[![BCH compliance](https://bettercodehub.com/edge/badge/AAYBS/GIC?branch=master)](https://bettercodehub.com/)
[![Known Vulnerabilities](https://snyk.io/test/github/AAYBS/GIC/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/AAYBS/GIC?targetFile=requirements.txt)
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
#login page configuration
[LOGIN]
USER_NAME='Your github user'
PASSWORD='Your github password'

#issue page configuration
[ISSUES]
TITLE='Issue title'
DESCRIPTION='Issue description'
```

## Running project
```
python creator.py
```
