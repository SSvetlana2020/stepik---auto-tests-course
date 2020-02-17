import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
	price = WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "100")
	)
	button = browser.find_element_by_id("book")
	button.click()
	
	#Пройти капчу для робота и получить число-ответ
	#Посчитать математическую функцию от x
	x_element=browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	#Ввести ответ в текстовое поле
	input2 = browser.find_element_by_id("answer")
	input2.send_keys(y)
	#нажимаем на кнопку
	browser.find_element_by_id("solve").click()
	browser.switch_to.alert
	time.sleep(1)
except Exception as error:
    print(f'Произошла ошибка, вот её описание: {error}')	
finally:
	time.sleep(30)
	browser.quit()