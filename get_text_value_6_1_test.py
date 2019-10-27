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


def test_3_6_1():
    logging.debug("test_3_6_1 was called")
    new_page("http://automationpractice.com/index.php")
    element = driver.find_element_by_class_name("login")
    print("Element text: " + element.text)
    # element_outer_html = element.get_attribute("outerHTML")
    # print("outerHTML: " + element_outer_html)
    driver.quit()


if __name__ == "__main__":
    test_3_6_1()
