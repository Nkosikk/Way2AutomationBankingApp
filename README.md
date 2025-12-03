# Way2Automation Banking App Tests

A simple Selenium + PyTest project that automates login and account selection for the Way2Automation Banking demo.

## Prerequisites
- Python 3.10+
- pip
- Browser driver on PATH (e.g., ChromeDriver, GeckoDriver, EdgeDriver, or Safari WebDriver)
- Google Chrome, Firefox, Edge, or Safari installed

## Install
- Create a virtual environment (optional)
- Install Python dependencies if needed (pytest, selenium)
  - pip install pytest selenium

## Configuration
Edit Configurations/data.ini:
- [URLS] dev_url: target URL
- [login data] yourName: visible customer name
- [user information] customerAccount1: account value to select after login

## Run Tests
- Run all dev-marked tests in Chrome:
  - pytest -m dev --browser=chrome
- Other browsers: --browser=firefox | edge | safari

## Project Structure
- Pages/: Page Objects for Login and Accounts
- tests/: PyTest tests and fixtures
- utils/: Config reader
- Configurations/: INI config

## Notes
- Ensure the correct WebDriver is installed and matches your browser version.
- If account selection should use visible text, implement select_account_by_text in Pages/accountPage.py and call it in tests.

## Testing
* testing again
