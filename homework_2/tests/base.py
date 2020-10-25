import pytest

from ui.pages.auth_page import AuthPage
from ui.pages.campaign_page import CampaignsPage
from ui.pages.new_campaigh_page import CreateNewCampaign
from ui.pages.segment_page import SegmentsPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config
        self.driver.implicitly_wait(10)

        self.auth_page: AuthPage = AuthPage(driver)
        self.campaign_page: CampaignsPage = CampaignsPage(driver)
        self.new_campaigh_page: CreateNewCampaign = CreateNewCampaign(driver)
        self.segment_page: SegmentsPage = SegmentsPage(driver)
