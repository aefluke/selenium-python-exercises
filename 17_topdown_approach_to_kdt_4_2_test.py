import logging
from selenium import webdriver, common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions \
    as EC

logging.basicConfig(level=logging.INFO)
driver = webdriver.Chrome()


def new_page(url):
    logging.debug("new_page was called")
    driver.get(url)
    logging.info("New Page:")
    logging.info("URL: " + driver.current_url)
    logging.info("Title: " + driver.title)


def doSearch(search_text):
    driver.find_element_by_xpath("//form[@id = 'searchbox']") \
        .click()
    driver.find_element_by_name("search_query") \
        .clear()
    driver.find_element_by_name("search_query") \
        .send_keys(search_text)


def itemAddtoCartByNum(item):
    driver.find_elements_by_xpath( \
        "//a[@title='Add to cart']")[item] \
        .click()


def test_4_4_2():
    url = "http://automationpractice.com"
    search_prompt = "printed dress"
    item_index = 0
    new_page(url)
    doSearch(search_prompt)
    itemAddtoCartByNum(item_index)
    assert len(driver.find_elements_by_xpath("//a[@title='Printed Summer Dress']")) > 0


driver.quit()
if __name__ == "__main__":
    test_4_4_2()
