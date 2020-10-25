import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.auth_page import AuthPage
from auth_data import EMAIL, LEGIT_PASSWORD


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    selenoid = config['selenoid_host_n_port']
    url = config['url']

    options = ChromeOptions()
    options.add_argument("--window-size=800,600")
    if selenoid is not None:
        host = selenoid[:selenoid.rfind(':')]
        port = selenoid[selenoid.rfind(':')+1:]
        print(host, port)
        driver = webdriver.Remote(command_executor=f'http://{host}:{port}/wd/hub/',
                                  options=options,
                                  desired_capabilities={'acceptInsecureCerts': True}
                                  )
    else:
        if browser == 'chrome':
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install(),
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True}
                                      )

        elif browser == 'firefox':
            manager = GeckoDriverManager(version=version)
            driver = webdriver.Firefox(executable_path=manager.install())

        else:
            raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def all_drivers(config, request):
    browser = request.param
    url = config['url']

    if browser == 'chrome':
        manager = ChromeDriverManager(version='latest')
        driver = webdriver.Chrome(executable_path=manager.install())

    elif browser == 'firefox':
        manager = GeckoDriverManager(version='latest')
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.maximize_window()
    driver.get(url)
    yield driver

    driver.quit()


# Фикстура для авторизации
@pytest.fixture(scope='function')
def auto_auth(driver):
    return AuthPage(driver).auth(EMAIL, LEGIT_PASSWORD)
