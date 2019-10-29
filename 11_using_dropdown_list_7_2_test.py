import logging

from selenium import webdriver

logging.basicConfig(level=logging.INFO)
driver = webdriver.Chrome()


def new_page(url):
    logging.debug("new_page was called")
    driver.get(url)
    logging.info("New Page:")
    logging.info("URL: " + driver.current_url)
    logging.info("Title: " + driver.title)


def test_3_7_2():
    logging.debug("test_3_7_2 was called")
    new_page("http://automationpractice.com/index.php?controller=prices-drop")
    element = driver.find_element_by_id("selectProductSort")
    element.click()
    path_string = "//*[@value = 'quantity:desc']"
    drop_element = driver.find_element_by_xpath(path_string)
    drop_element.click()
    # determine that page opened is the correct page
    assert "orderby=quantity" in driver.current_url, "Incorrect page opened"
    driver.quit()


if __name__ == "__main__":
    test_3_7_2()
