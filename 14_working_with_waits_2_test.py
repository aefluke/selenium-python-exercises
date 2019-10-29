import logging
from time import sleep

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


def test_4_2():
    new_page("https://www.python.org/")
    search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id-search-field")))
    search_box.clear()
    search_box.send_keys("comprehensions")
    button_go = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
    button_go.click()
    sleep(3)
    driver.quit()


if __name__ == "__main__":
    test_4_2()
