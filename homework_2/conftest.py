from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='http://www.target.my.com')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=None)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid_host_n_port = request.config.getoption('--selenoid')
    return {'browser': browser, 'version': version, 'url': url, 'selenoid_host_n_port': selenoid_host_n_port}