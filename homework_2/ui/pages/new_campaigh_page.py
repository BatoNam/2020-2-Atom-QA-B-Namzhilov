import os

from ui.locators.locators import TrafficCampaignCreationLocators
from ui.pages.base_page import BasePage


class CreateNewCampaign(BasePage):
    locators = TrafficCampaignCreationLocators()

    def campaign_creation(self, camp_name):
        self.click(self.locators.TRAFFIC_BUTTON)
        self.placeholder_send_keys(self.locators.INPUT_URL, 'https://www.mephi.ru/')
        self.placeholder_send_keys(self.locators.INPUT_CAMPAIGN_NAME, camp_name)
        self.placeholder_send_keys(self.locators.INPUT_DAILY_BUDGET, '100')
        self.placeholder_send_keys(self.locators.INPUT_DAILY_TOTAL, '1000')

        self.click(self.locators.MULTIFORMAT_BUTTON)
        self.placeholder_send_keys(self.locators.INPUT_TITLE, 'Title example')
        self.placeholder_send_keys(self.locators.INPUT_TEXT, 'Text example')

        path_to_image = os.path.dirname(os.path.abspath(__file__)) + '/image_source/'
        self.placeholder_send_keys(self.locators.LOAD_CONTENT, path_to_image + '256.jpg', image=True)
        self.placeholder_send_keys(self.locators.LOAD_PROMOCONTENT, path_to_image + '1080.jpg', image=True)
        self.placeholder_send_keys(self.locators.LOAD_ICON, path_to_image + '600.jpg', image=True)
        self.click(self.locators.CREATE_COMPANY_END_BUTTON)
