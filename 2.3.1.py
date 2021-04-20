from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def ex165(link):
    browser.get(link)

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
    assert "Congratulations! You have successfully registered!" == welcome_text


def ex232(link):
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    # parse x
    x = int(browser.find_element_by_id("input_value").text)
    result = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


def ex233(link):
    browser.get(link)

    button = browser.find_element_by_css_selector("button.trollface")
    button.click()

    # switch to the new tab
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # parse x
    x = int(browser.find_element_by_id("input_value").text)
    result = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)

    click_button("solve")


def ex241(link):
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button = browser.find_element_by_id("book")
    button.click()

    # parse x
    x = int(browser.find_element_by_id("input_value").text)
    print(str(x))
    result = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)

    click_button("solve")


def click_button(name):
    button = browser.find_element_by_id(name)
    button.click()


try:
    browser = webdriver.Chrome(
        r"A:\REDHAWK\Desktop\СибАДИ\Магистратура\2 semester\Тестирование ПО - Пестова С.Ю\Stepik Selenium\chromedriver.exe")

    # Part 1
    #ex165("http://suninjuly.github.io/registration1.html")
    ex165("http://suninjuly.github.io/registration2.html")

    # Part 2
    # ex232("http://suninjuly.github.io/alert_accept.html")
    # ex233("http://suninjuly.github.io/redirect_accept.html")
    #ex241("http://suninjuly.github.io/explicit_wait2.html")


except Exception as error:
    print(error)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
