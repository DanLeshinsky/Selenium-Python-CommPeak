import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        if self.PAGE_URL:
            self.driver.get(self.PAGE_URL)
        else:
            print("Not possible to open page without url")

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def is_opened_search_query(self, q):
        self.wait.until(EC.url_contains(f"{self.PAGE_URL}/search?q={q}"))
