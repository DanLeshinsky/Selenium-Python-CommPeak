from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC  # Add this line
from base.base_page import BasePage
from config.links import Links


class GooglePage(BasePage):

    PAGE_URL = Links.GOOGLE_URL
    SEARCH_BOX = (By.NAME, 'q')


    def search(self, query):
        search_box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BOX))
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)