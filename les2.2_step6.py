# -*- coding: utf-8 -*-
# !/usr/bin/env python3

# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import math
from selenium import webdriver
from time import sleep


link = 'https://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    x_el = browser.find_element_by_id('input_value').text
    # x_el = browser.find_element_by_css_selector('img[id="treasure"]')  # +
    # val = x_el.get_attribute('input_value')
    # x_element = browser.find_element_by_id('input_value')
    # x = x_element.text
    y = calc(x_el)
    result = browser.find_element_by_id('answer')
    result.send_keys(y)

    # submit = browser.find_element_by_tag_name('button')
    submit = browser.find_element_by_css_selector('button.btn')
    # прокрутка, чтобы кнопка была видна
    browser.execute_script('return arguments[0].scrollIntoView(true);', submit)

    checkbox = browser.find_element_by_id(
        'robotCheckbox').click()
    # checkbox = browser.find_element_by_css_selector(
    #     '[for="robotCheckbox"]').click()  # +

    radiobtn = browser.find_element_by_id('robotsRule').click()

    # submit = browser.find_element_by_css_selector('button.btn')
    # submit = browser.find_element_by_tag_name('button')
    # browser.execute_script('return arguments[0].scrollIntoView(true);', submit)
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    # alert.accept()
    print(alert_text)

    # people_radio = browser.find_element_by_id("peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked == 'true', "People radio is not selected by default"

    # robots_radio = browser.find_element_by_id("robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None

finally:
    sleep(10)
    browser.quit()
