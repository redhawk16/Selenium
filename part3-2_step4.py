from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        first_block = browser.find_element_by_css_selector("div.first_block")
        second_block = browser.find_element_by_css_selector("div.second_block")

        first_block.find_element_by_css_selector("input.first").send_keys("first_first")
        first_block.find_element_by_css_selector("input.second").send_keys("first_second")
        first_block.find_element_by_css_selector("input.third").send_keys("first_third")

        second_block.find_element_by_css_selector("input.first").send_keys("second_first")
        second_block.find_element_by_css_selector("input.second").send_keys("second_second")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Message should be equals")


    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        first_block = browser.find_element_by_css_selector("div.first_block")
        second_block = browser.find_element_by_css_selector("div.second_block")

        first_block.find_element_by_css_selector("input.first").send_keys("first_first")
        first_block.find_element_by_css_selector("input.second").send_keys("first_second")
        first_block.find_element_by_css_selector("input.third").send_keys("first_third")

        second_block.find_element_by_css_selector("input.first").send_keys("second_first")
        second_block.find_element_by_css_selector("input.second").send_keys("second_second")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Message should be equals")


if __name__ == "__main__":
    unittest.main()