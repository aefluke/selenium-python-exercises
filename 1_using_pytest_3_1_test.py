import logging
import time

import pytest

logging.basicConfig(level=logging.INFO)


@pytest.mark.skip
def test_3_1():
    logging.info("running test 3_1")
    current_time = time.localtime()
    logging.info("current time: " +
                 str(current_time.tm_mday) + "-" +
                 str(current_time.tm_mon) + "-" +
                 str(current_time.tm_year) + " " +
                 str(current_time.tm_hour) + ":" +
                 str(current_time.tm_min) + ":" +
                 str(current_time.tm_sec)
                 )
    assert current_time.tm_hour < 12, "Current time should be before noon"
