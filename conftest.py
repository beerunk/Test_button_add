import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default = "ru",
                     help="Choose language: es or fr")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = request.config.getoption("browser_name")
    #browser = None
    if browser == "chrome":
        print("\nstart es language for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser == "firefox":
        print("\nstart fr language for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()

