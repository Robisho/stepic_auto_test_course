# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

url = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(url)

try:
    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)
    # print(num1, num2)

    res = str(num1 + num2)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(res)

    submit = browser.find_element_by_css_selector('button.btn').click()

finally:
    sleep(7)
    browser.quit()
