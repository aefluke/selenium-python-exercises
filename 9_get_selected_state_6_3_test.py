import logging
from time import sleep

from selenium import webdriver

logging.basicConfig(level=logging.INFO)
driver = webdriver.Chrome()


def new_page(url):
    logging.debug("new_page was called")
    driver.get(url)
    logging.info("New Page:")
    logging.info("URL: " + driver.current_url)
    logging.info("Title: " + driver.title)


def test_3_6_3():
    logging.debug("test_3_6_3 was called")
    new_page("http://automationpractice.com/index.php?id_category=8&controller=category#/\
    categories-casual_dresses/compositions-cotton")
    element = driver.find_element_by_id("layered_id_attribute_group_1")
    element_state = element.is_selected()
    print("Selected: " + str(element_state))
    print("Now click the Size S checkbox")
    sleep(30)
    element = driver.find_element_by_id("layered_id_attribute_group_1")
    element_state = element.is_selected()
    print("Selected: " + str(element_state))
    driver.quit()


if __name__ == "__main__":
    test_3_6_3()
