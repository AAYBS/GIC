[![BCH compliance](https://bettercodehub.com/edge/badge/AAYBS/GIC?branch=master)](https://bettercodehub.com/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4edd05c3ba8d409485e1c338741dfaf2)](https://www.codacy.com/app/ZoranPandovski/GIC?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AAYBS/GIC&amp;utm_campaign=Badge_Grade)
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

#issue pasge configuration
[ISSUES]
TITLE='Issue title'
DESCRIPTION='Issue description'
```

## Running project
```
python creator.py
```
