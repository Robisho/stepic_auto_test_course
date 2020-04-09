# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from selenium import webdriver
from time import sleep
import math

url = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(url)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    button = browser.find_element_by_css_selector('button.btn').click()

    confirm = browser._switch_to.alert
    confirm.accept()

    url = 'http://suninjuly.github.io/alert_redirect.html'
    browser.get(url)

    x = browser.find_element_by_id('input_value').text
    res = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(res)

    submit = browser.find_element_by_css_selector('button.btn').click()

    alert = browser._switch_to.alert
    alert_txt = alert.text
    print(alert_txt)

finally:
    sleep(7)
    browser.quit()  #
