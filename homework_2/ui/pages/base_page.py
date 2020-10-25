from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


RETRY_COUNT = 3


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        # попытки чтобы кликнуть
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def placeholder_send_keys(self, locator, keys, timeout=10, clear=True, image=False):
        placeholder = self.find(locator)
        if not image:
            placeholder.clear()
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
        placeholder.send_keys(keys)
