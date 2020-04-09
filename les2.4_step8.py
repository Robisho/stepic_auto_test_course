# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился, то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.

'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(url)

try:
    # драйвер ждет до 12сек, пока не появится id='price' со значением '$100'
    price = WebDriverWait(browser, timeout=12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element_by_id('book').click()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    submit = browser.find_element_by_id('solve').click()

    alert = browser.switch_to.alert
    alert_txt = alert.text
    print(alert_txt)

finally:
    browser.quit()
