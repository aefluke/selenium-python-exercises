import logging

import pytest
from selenium import webdriver


@pytest.mark.skip
def test_3_3_2():
    logging.debug("test_3_3_2 was called")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.switch_to.frame("iframeResult")
    driver.find_element_by_css_selector('[onclick*="myFunction()"]')
    driver.switch_to.default_content()
    assert "Tryit Editor" in driver.title
    driver.quit()


if __name__ == "__main__":
    test_3_3_2()
