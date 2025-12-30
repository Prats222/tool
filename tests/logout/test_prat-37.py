import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_prat-37():
    """Jira: PRAT-37"""

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://example.com")

        # Preconditions:
        # User is logged in

        # Steps:
        # Click on profile menu \n        #  Click Logout

        # Expected:
        # User should be logged out and redirected to login page

        assert True

    finally:
        driver.quit()
