# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from selenium import webdriver
from time import sleep
import os


url = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(url)

try:
    fname = browser.find_element_by_name('firstname')
    fname.send_keys('tututu')

    lname = browser.find_element_by_name('lastname')
    lname.send_keys('nanana')

    email = browser.find_element_by_name('email')
    email.send_keys('tututu@nanana.com')

    upfile = browser.find_element_by_id('file')  # выбрали загрузку файла
    # определили папку, где файл лежит, он там же, где и скрипт
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # определили путь к файлу
    file_path = os.path.join(current_dir, 'file.txt')
    upfile.send_keys(file_path)  # отдали путь к файлу

    submit = browser.find_element_by_css_selector('button.btn').click()

finally:
    sleep(5)
    browser.quit()
