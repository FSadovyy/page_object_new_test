import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox
driver = webdriver.Chrome(service=Service(), options=webdriver.ChromeOptions())


def pytest_addoption(parser):
    
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")
    
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help="Choose language") 
    
@pytest.fixture(scope="function")
def browser(request):
    browser = None
    user_language = request.config.getoption("language")
    print(f"\nwith {user_language} as interface language..")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = OptionsChrome()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        print ("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", user_language)
        print ("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else: 
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
    driver.quit()



    
