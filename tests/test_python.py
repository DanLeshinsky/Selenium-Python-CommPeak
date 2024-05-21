import os
import pytest
import utilities.utilities as utils
from base.base_test import BaseTest


class TestPythonDownloads(BaseTest):

    @pytest.mark.smoke
    def test_python_downloads_page(self):
        search_query = "python"
        self.google_page.open()
        self.google_page.search(search_query)
        self.google_search_result_page.is_opened_search_query(search_query)
        self.google_search_result_page.click_python_org_downloads()
        self.python_org_downloads_page.is_opened()
        button_version = self.python_org_downloads_page.get_download_button_version()
        button_href = self.python_org_downloads_page.get_download_button_href()
        expected_href = f"https://www.python.org/ftp/python/{button_version}/python-{button_version}-amd64.exe"
        assert button_href == expected_href, f"Expected {expected_href}, but got {button_href}"
        self.python_org_downloads_page.check_python_version_eos("3.8", "2024-10")

    @pytest.mark.smoke
    def test_download_and_verify_md5(self):

        self.python_release_page.open()
        self.python_release_page.is_opened()

        files_dir = os.path.join(os.path.dirname(__file__), '../files')
        if not os.path.exists(files_dir):
            os.makedirs(files_dir)

        download_url, expected_md5_checksum = self.python_release_page.get_gzipped_source_url()
        file_name = download_url.split("/")[-1]
        file_path = utils.download_file(download_url, files_dir, file_name)
        calculated_md5 = utils.get_md5_checksum(file_path)

        try:
            assert expected_md5_checksum == calculated_md5, f"Expected MD5 checksum {expected_md5_checksum}, but got {calculated_md5}"
            print("Your file is secure.")
        except AssertionError as e:
            print(str(e))
            raise
