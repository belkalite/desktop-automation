# Desktop Python Automation for MacOS

Appium-based automation framework for MacOS decktop applications.
For demo proposals Reverso application is used https://context.reverso.net/

## Getting started

Prerequisites:

1. МacOS over 10.15
2. Python 3.7 or greater is required.
3. Install and run appium-for-mac:
https://github.com/appium/appium-for-mac
4. Install Reverso application and give permission to open the app downloaded from the Internet:

```brew install --cask reverso```

Create your virtualenv, activate and install dependencies:

```pip install -r requirements.txt```

Run tests:

```pytest tests```

Run tests and save Allure report:

```pytest --alluredir=allure_report tests```

To clean the results of previous run:

```pytest --alluredir=allure_report --clean-alluredir tests```

Allure report results:

```allure serve allure_report```