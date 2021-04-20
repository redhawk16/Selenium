from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(r"A:\REDHAWK\Desktop\СибАДИ\Магистратура\2 semester\Тестирование ПО - Пестова С.Ю\Stepik Selenium\chromedriver.exe")
    browser.get(link)

    x = int(browser.find_element_by_id("input_value").text)
    result = calc(x)

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input = browser.find_element_by_id("answer")
    input.send_keys(result)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # browser.execute_script("alert('Robots at work');")

    # scroll to view
    # button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()

    button.click()

except Exception as error:
    print(error)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла