import logging

import pytest
from selenium import webdriver

logging.basicConfig(level=logging.INFO)


@pytest.mark.skip
def test_3_3_1():
    driver = webdriver.Chrome()
    logging.debug("test_3_3_1 was called")
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.switch_to.frame("iframeResult")
    driver.find_element_by_css_selector('[onclick*="myFunction()"]')
    driver.switch_to.default_content()
    assert "Tryit Editor" in driver.title
    driver.quit()


if __name__ == "__main__":
    test_3_3_1()
