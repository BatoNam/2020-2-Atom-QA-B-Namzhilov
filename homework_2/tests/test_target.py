import pytest
import time
from selenium.common.exceptions import TimeoutException
from datetime import datetime

from tests.base import BaseCase
from auth_data import EMAIL, LEGIT_PASSWORD, FALSE_PASSWORD


class Test(BaseCase):
    @pytest.mark.UI
    def test_auth_positive(self):
        locator = self.auth_page.locators.EMAIL_AFTER_AUTH
        self.auth_page.auth(EMAIL, LEGIT_PASSWORD)
        assert self.auth_page.find(locator)

    @pytest.mark.UI
    def test_auth_negative(self):
        locator = self.auth_page.locators.EMAIL_AFTER_AUTH
        self.auth_page.auth(EMAIL, FALSE_PASSWORD)
        with pytest.raises(TimeoutException):
            assert self.auth_page.find(locator)

    @pytest.mark.UI
    def test_campaign_creation(self, auto_auth):
        locator = self.campaign_page.locators.CHECK_NAME_OF_COMPANY
        company_name = str(datetime.now())
        self.campaign_page.create_new_company()
        self.new_campaigh_page.campaign_creation(company_name)
        assert company_name == self.campaign_page.find(locator).text

    @pytest.mark.UI
    def test_segment_creation(self, auto_auth):
        locator = self.segment_page.locators.SEGMENT_NAME
        segment_name = str(datetime.now())
        self.campaign_page.go_to_segments_page()
        self.segment_page.segment_creation(segment_name)
        assert segment_name == self.segment_page.find(locator).text

    @pytest.mark.UI
    def test_segment_delete(self, auto_auth):
        segment_name = str(datetime.now())
        self.campaign_page.go_to_segments_page()
        self.segment_page.segment_creation(segment_name)
        self.segment_page.segment_delete()
        # Иначе выводит удаленное имя
        time.sleep(3)
        locator = self.segment_page.locators.SEGMENT_NAME
        try:
            segment_name_after = self.segment_page.find(locator).text
            assert segment_name != segment_name_after
        except TimeoutException:
            with pytest.raises(TimeoutException):
                assert self.segment_page.find(locator)
