### Test Automation Scenarios for Testing QA Test App

This a project for web automation of [Qa Test App](https://qa-task.netlify.app/).

Technology stack: [Python](https://www.python.org/), [Selenium](https://www.selenium.dev/), 
[Behave](https://pypi.org/project/behave/)


### Structure

```
Project Folder
├── features
│   ├── pages
│   │   ├── base_page.py    # base class - helper functions
│   │   ├── home.page.py    # homepage class with locators dictionary
│   ├── steps
│   │   ├── qatest_steps.py # Gherkin steps
│   ├── qatest.feature      # test scenarios
│   ├── environment.py      # browser settings 
├── test_data.py            # test data, usernames etc.
```

### Local env setup

Tu use this project Python 3.X. is required.

MacOS
```bash
python3.8 -m venv venv
source venv/bin/activate
pip install pip-tools
pip install -r requirements.txt
```

Windows
```bash
python3.8 -m venv venv
\path\to\env\Scripts\activate
example: C:\Users\Username\venv\Scripts\activate.bat
pip install pip-tools
pip install -r requirements.txt
```

The convention for managing Python dependency is as follows:
- we add the dependency into requirements.in
- we call ```pip-compile``` or ```python3.8 -m piptools compile``` to create requirements.txt
- we commit both files to repository.


To run tests locally Selenium Webdriver is required. 
In this project Selenium Webdriver is managed automatically by 
[Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager)
Be sure that you have updated version of [Chrome Browser](https://www.google.com/chrome/) on your device.

### How to run?

Just type in the command line

```
behave
```
