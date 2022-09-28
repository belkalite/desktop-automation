# Desktop Python Automation for MacOS

Appium-based automation framework for MacOS decktop applications.
For demo proposals Reverso application is used https://context.reverso.net/

## Getting started

Prerequisites:

1. Python 3.7 or greater is required.
2. Install and run appium-for-mac:
https://github.com/appium/appium-for-mac
3. Install Reverso application and give permission to open the app downloaded from the Internet:

```brew install --cask reverso```

Create your virtualenv, activate and install dependencies:

```pip install -r requirements.txt```

Test run and save Allure report:

```pytest --alluredir=allure_report --clean-alluredir tests/test_reverso.py```

Allure report results:

```allure serve allure_report```