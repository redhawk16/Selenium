from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(r"A:\REDHAWK\Desktop\СибАДИ\Магистратура\2 semester\Тестирование ПО - Пестова С.Ю\Stepik Selenium\chromedriver.exe")
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("firstname")
    browser.find_element_by_name("lastname").send_keys("lastname")
    browser.find_element_by_name("email").send_keys("email")

    fileUpl = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    fileUpl.send_keys(file_path)

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