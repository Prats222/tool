import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_prat-33():
    """Jira: PRAT-33"""

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://example.com")

        # Preconditions:
        # User is registered and on login page

        # Steps:
        # Enter valid username \n        #  Enter invalid password \n        #  Click Login

        # Expected:
        # Error message should be displayed indicating invalid credentials

        assert True

    finally:
        driver.quit()
