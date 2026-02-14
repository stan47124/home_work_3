import pytest
from selenium import webdriver


@pytest.mark.selenium
def test_selenium():
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/")

    assert driver.title == "Selenium"
    assert driver.current_url == "https://www.selenium.dev/"
