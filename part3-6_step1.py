from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class Test():
    stroka = ""

    @pytest.mark.parametrize('link', [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ])
    def test_case(self, browser, link):
        browser.get(link)

        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )  # Wait until the `text_to_score` element appear (up to 5 seconds)

        answer = math.log(int(time.time()))
        textarea = browser.find_element_by_tag_name('textarea')
        textarea.send_keys(f"{answer}")

        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()

        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "pre"))
        )
        tx = browser.find_element_by_tag_name("pre").text
        if (tx != "Correct!"):
            self.stroka += f"{tx}"
            print(f"{self.stroka}")

        assert tx == "Correct!"
