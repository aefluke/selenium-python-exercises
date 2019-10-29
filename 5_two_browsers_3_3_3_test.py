import logging

import pytest
from selenium import webdriver


@pytest.mark.skip
def test_3_3_3():
    br1 = webdriver.Chrome()
    br2 = webdriver.Chrome()
    logging.debug("running test_3_3")
    # open python 2 /library
    br1.get("https://docs.python.org/2/library/functions.html")

    # open python 3 /library
    br2.get("https://docs.python.org/3/library/functions.html")
    br2.switch_to.window("")
    # should be found
    elements = br1.find_elements_by_partial_link_text('reload')
    # At least one element that matches should be found
    assert len(elements) > 0, "Reload function could not be found"
    # should not be found
    elements = br2.find_elements_by_partial_link_text('reload')
    # No elements that match should be found
    assert len(elements) == 0, "Reload function was found but not expected"
    br1.quit()
    br2.quit()


if __name__ == "__main__":
    test_3_3_3()
