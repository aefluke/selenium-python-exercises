import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)
driver = webdriver.Chrome()


def new_page(url):
    logging.debug("new_page was called")
    driver.get(url)
    logging.info("New Page:")
    logging.info("URL: " + driver.current_url)
    logging.info("Title: " + driver.title)


def test_3_5_1():
    logging.debug("test_3_5_1 was called")
    new_page("http://www.automationpractice.com/index.php")
    try:
        driver.find_element_by_id("search_query_top")
        print("The element has been found")
    except NoSuchElementException:
        print("The element has not been found")
        driver.quit()


if __name__ == "__main__":
    test_3_5_1()
