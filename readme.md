# GitHub Issue Creator
This project automates the creation of repetitive tasks, as creating GitHub issues to get more contributors. Page Object Model is used as a design pattern which has become popular in test automation for enhancing test maintenance and reducing code duplication. For more information read: [PageObjects](https://github.com/SeleniumHQ/selenium/wiki/PageObjects)

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
