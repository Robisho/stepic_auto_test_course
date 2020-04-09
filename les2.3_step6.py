# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from selenium import webdriver
from time import sleep
import math


url = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(url)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    button = browser.find_element_by_css_selector('button.trollface').click()

    # browser.switch_to.window(new_w)
    new_w = browser.window_handles[1]
    browser.switch_to.window(new_w)
    odl_w = browser.window_handles[0]

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    submit = browser.find_element_by_css_selector('button.btn').click()

    alert = browser.switch_to.alert
    a_text = alert.text
    print(a_text)

finally:
    sleep(7)
    browser.quit()
