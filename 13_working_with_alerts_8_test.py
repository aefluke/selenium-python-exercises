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


def test_3_8():
    new_page("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.switch_to.frame("iframeResult")
    target = '[onclick*="myFunction()"]'
    try_it_button = driver. \
        find_element_by_css_selector(target)
    try_it_button.click()
    alert = driver.switch_to.alert
    assert "Hello!" in alert.text, "Incorrect text"
    alert.dismiss()
    driver.quit()


if __name__ == "__main__":
    test_3_8()
