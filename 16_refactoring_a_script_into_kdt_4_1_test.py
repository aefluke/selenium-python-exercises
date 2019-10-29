from time import sleep

from selenium import webdriver


def open_page(driver, url):
    driver.get(url)


def search_for(driver, search):
    search_box = "search_query_top"
    driver.find_element_by_id(search_box).click()
    driver.find_element_by_id(search_box).clear()
    driver.find_element_by_id(search_box).send_keys(search)
    driver.find_element_by_name("submit_search").click()


def add_to_cart(driver):
    add_to_cart = "//div[@id='center_column']/ul/li/div/div[2]/div[2]/a/span"
    driver.find_element_by_xpath(add_to_cart).click()


def test_app_dynamics_job():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    target_site = \
        "http://automationpractice.com/index.php?"
    search = "printed dress"
    open_page(driver, target_site)
    search_for(driver, search)
    add_to_cart(driver)
    sleep(10)
    driver.quit()


if __name__ == "__main__":
    test_app_dynamics_job()
