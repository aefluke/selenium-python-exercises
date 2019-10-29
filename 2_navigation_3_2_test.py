import logging

import pytest
from selenium import webdriver


@pytest.mark.skip
def test_3_2():
    driver = webdriver.Chrome()
    logging.debug("running test_3_2")
    driver.get("https://docs.python.org/")
    logging.info("URL: " + driver.current_url)
    logging.info("Title: " + driver.title)
    assert "Documentation" in driver.title
    driver.quit()


if __name__ == "__main__":
    test_3_2()
