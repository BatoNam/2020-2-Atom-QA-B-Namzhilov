from selenium.common.exceptions import TimeoutException

from ui.locators.locators import SegmentsPageLocators
from ui.pages.base_page import BasePage


class SegmentsPage(BasePage):
    locators = SegmentsPageLocators()

    def segment_creation(self, name):
        try:
            self.click(self.locators.CREATE_FIRST_SEGMENT_BEGIN)
        except TimeoutException:
            self.click(self.locators.CREATE_SEGMENT_BEGIN)

        self.click(self.locators.APPS_N_GAMES)
        self.click(self.locators.PLATFROM_OPTIONS_BUTTON)
        self.click(self.locators.CHECKBOX_PAY)
        self.click(self.locators.CREATE_SEGMENT_MIDDLE)

        self.placeholder_send_keys(self.locators.INPUT_NAME_SEGMENT, name)
        self.click(self.locators.CREATE_SEGMENT_END)

    def segment_delete(self):
        self.click(self.locators.DELETE_CROSS_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_SEGMENT)
