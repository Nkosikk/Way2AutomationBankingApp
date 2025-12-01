import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser.lower() == 'edge':
        driver = webdriver.Edge()

    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Safari()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
