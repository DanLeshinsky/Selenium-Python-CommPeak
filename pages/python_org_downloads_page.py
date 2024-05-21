from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class PythonOrgDownloadsPage(BasePage):

    PAGE_URL = Links.PYTHON_DOWNLOADS_URL
    DOWNLOAD_BUTTON = (By.XPATH, "//p[@class='download-buttons']//a[@class='button' and contains(@href, 'python-3.12.3-amd64.exe')]")
    ACTIVE_PYTHON_RELEASES_LIST = (By.XPATH, '//div[@class="row active-release-list-widget"]//ol[@class="list-row-container menu"]')

    def get_download_button_version(self):
        button = self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_BUTTON))
        return button.text.split()[-1]

    def get_download_button_href(self):
        button = self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_BUTTON))
        return button.get_attribute('href')

    def check_python_version_eos(self, version, expected_eos):
        list_container = self.wait.until(EC.visibility_of_element_located(self.ACTIVE_PYTHON_RELEASES_LIST))
        items = list_container.find_elements(By.TAG_NAME, 'li')
        for item in items:
            version_span = item.find_element(By.CSS_SELECTOR, "span.release-version")
            if version_span.text.strip() == version:
                eos_span = item.find_element(By.CSS_SELECTOR, "span.release-end")
                eos = eos_span.text.strip()
                assert eos == expected_eos, f"Expected end of support: {expected_eos}, but got: {eos}"
                return True
        raise AssertionError(f"Python version {version} not found in Active Python Releases list.")