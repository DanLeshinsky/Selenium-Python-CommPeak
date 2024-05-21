import pytest
from pages.google_page import GooglePage
from pages.google_search_result_page import GoogleSearchResultPage
from pages.python_org_downloads_page import PythonOrgDownloadsPage
from pages.python_release_page import PythonReleasePage


class BaseTest:

    google_page: GooglePage
    google_search_result_page: GoogleSearchResultPage
    python_org_downloads_page: PythonOrgDownloadsPage
    python_release_page: PythonReleasePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver

        request.cls.google_page = GooglePage(driver)
        request.cls.google_search_result_page = GoogleSearchResultPage(driver)
        request.cls.python_org_downloads_page = PythonOrgDownloadsPage(driver)
        request.cls.python_release_page = PythonReleasePage(driver)
