import logging

import requests
from selenium import webdriver

logging.basicConfig(level=logging.INFO)
driver = webdriver.Chrome()


def new_page(url):
    logging.debug("new_page was called")
    driver.get(url)
    logging.info("New Page:")
    logging.info("URL: " + driver.current_url)
    logging.info("Title: " + driver.title)


def test_image_sources():
    new_page("http://www.automationpractice.com/index.php")

    images = driver.find_elements_by_class_name("img-responsive")
    for image in images:
        image_source = image.get_attribute("src")
        response = requests.get(image_source)
        logging.info(image_source + " --> " + str(response.status_code))
        assert response.status_code == 200
    driver.quit()


if __name__ == "__main__":
    test_image_sources()
