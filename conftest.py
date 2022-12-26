import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OpChrome
from selenium.webdriver.firefox.options import Options as OpFireFox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox"
                     )
    parser.addoption('--language', action='store',
                       default='en',
                       help="user_language: ru or en"
                       )

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == 'chrome':
        print('\nStart Chrom browser for test..')
        options = OpChrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        print('\nStart FireFox browser for test..')
        options = OpFireFox()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be Chrome or FireFox")
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")
    browser.quit()