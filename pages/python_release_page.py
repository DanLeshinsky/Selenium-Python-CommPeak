from typing import Tuple
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PythonReleasePage(BasePage):

    PAGE_URL = Links.PYTHON_RELEASE_PAGE
    GZIPPED_SOURCE_BUTTON = (By.XPATH, "//a[contains(text(),'Gzipped source tarball')]")

    def get_gzipped_source_url(self) -> Tuple[ str, str]:
        gzipped_source_button = self.wait.until(EC.element_to_be_clickable(self.GZIPPED_SOURCE_BUTTON))
        url = gzipped_source_button.get_attribute('href')
        md5_sum_element = gzipped_source_button.find_element(By.XPATH, "../following-sibling::td[3]")
        md5_sum = md5_sum_element.text.strip()
        return url, md5_sum