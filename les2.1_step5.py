# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import math
from selenium import webdriver
from time import sleep


link = 'http://suninjuly.github.io/get_attribute.html'
# link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    x_el = browser.find_element_by_id('treasure')
    # x_el = browser.find_element_by_css_selector('img[id="treasure"]')  # +
    val = x_el.get_attribute('valuex')
    # x_element = browser.find_element_by_id('input_value')
    # x = x_element.text
    y = calc(val)
    result = browser.find_element_by_id('answer')
    result.send_keys(y)

    checkbox = browser.find_element_by_id(
        'robotCheckbox').click()
    # checkbox = browser.find_element_by_css_selector(
    #     '[for="robotCheckbox"]').click()  # +

    radiobtn = browser.find_element_by_id('robotsRule').click()

    submit = browser.find_element_by_css_selector('button.btn')
    submit.click()

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == 'true', "People radio is not selected by default"

    # robots_radio = browser.find_element_by_id("robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None

finally:
    sleep(10)
    browser.quit()
