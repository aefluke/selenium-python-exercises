import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(level=logging.INFO)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()


def new_page(url):
    logging.debug("new_page was called")
    driver.get(url)
    logging.info("New Page:")
    logging.info("URL: " + driver.current_url)
    logging.info("Title: " + driver.title)


def test_3_7_3():
    logging.debug("test_3_7_3 was called")
    new_page("http://automationpractice.com")
    driver.find_element_by_partial_link_text("Faded Short Sleeve\ T-shirts").click()
    driver.find_element_by_css_selector("#add_to_cart >\ button").click()
    modal = driver.find_element_by_id("layer_cart")
    element = WebDriverWait(modal, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Proceed to checkout']")))
    element.click()
    assert driver.title == "Order - My Store", "Checkout page is\ not open"
    driver.quit()


if __name__ == "__main__": test_3_7_3()
