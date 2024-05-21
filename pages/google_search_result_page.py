from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links


class GoogleSearchResultPage(BasePage):

    PAGE_URL = Links.GOOGLE_URL
    DOWNLOADS = (By.XPATH, "//div[@id='search']//span[contains(text(),'Downloads')]")


    def click_python_org_downloads(self):
        link = self.wait.until(EC.element_to_be_clickable(self.DOWNLOADS))
        link.click()
