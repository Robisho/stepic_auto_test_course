# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/huge_form.html')
    elements = browser.find_elements_by_tag_name('input')
    for el in elements:
        el.send_keys('Мой ответ')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    # успеваем за 30 сек копирнуть
    time.sleep(30)
    # закрываем браузер
    browser.quit()
