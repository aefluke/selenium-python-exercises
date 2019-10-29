import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(level=logging.INFO)
driver = webdriver.Chrome()


def new_page(url):
    logging.debug("new_page was called")
    driver.get(url)
    logging.info("New Page:")
    logging.info("URL: " + driver.current_url)
    logging.info("Title: " + driver.title)


def test_3_7_1():
    logging.debug("test_3_7_1 was called")

    new_page("http://automationpractice.com/index.php")
    element = (WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "login"))))
    element.click()
    # determine that page opened is the correct page
    logging.info("URL: " + driver.current_url)
    assert "authentication" in driver.current_url, "Incorrect page opened"
    driver.quit()


if __name__ == "__main__":
    test_3_7_1()
