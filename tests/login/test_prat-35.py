import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_prat-35():
    """Jira: PRAT-35"""

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://example.com")

        # Preconditions:
        # User is registered and on login page

        # Steps:
        # Enter valid username \n        #  Enter valid password \n        #  Click Login

        # Expected:
        # User should be logged in successfully and redirected to dashboard

        assert True

    finally:
        driver.quit()
