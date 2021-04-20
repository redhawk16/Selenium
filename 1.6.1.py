from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(r"A:\REDHAWK\Desktop\СибАДИ\Магистратура\2 semester\Тестирование ПО - Пестова С.Ю\Stepik Selenium\chromedriver.exe")
    browser.get(link)

    value1 = browser.find_element_by_id("num1").text
    value2 = browser.find_element_by_id("num2").text
    result = int(value1) + int(value2)
    print(result)

    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(str(result))  # ищем элемент с текстом "Python"

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except Exception as error:
    print(error)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла