from selenium.common.exceptions import TimeoutException

from ui.locators.locators import CampaignsPageLocators
from ui.pages.base_page import BasePage


class CampaignsPage(BasePage):
    locators = CampaignsPageLocators()

    def go_to_campaigns_page(self):
        self.click(self.locators.CAMPAIGNS_BUTTON)

    def go_to_segments_page(self):
        self.click(self.locators.SEGMENTS_BUTTON)

    def create_new_company(self):
        try:
            self.click(self.locators.CREATE_CAMPAIGN_BEGIN)
        except TimeoutException:
            self.click(self.locators.CREATE_FIRST_CAMPAIGN_BEGIN)
        return
