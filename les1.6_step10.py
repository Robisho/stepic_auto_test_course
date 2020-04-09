# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from selenium import webdriver
import time

try:
    # link = "http://suninjuly.github.io/registration2.html"
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    # block1
    fname = browser.find_element_by_class_name('first')
    fname.send_keys('tututu')
    time.sleep(1)

    # lname = browser.find_element_by_xpath(
    #     '//input[@placeholder="Input your last name"]')  # +
    lname = browser.find_element_by_css_selector(
        '.first_block .second_class .second')  # рабочий
    # lname = browser.find_element_by_css_selector('input.second')  # рабочий
    # lname = browser.find_element_by_class_name('second')  # рабочий
    # lname = browser.find_element_by_css_selector("[placeholder*='first name']")  # чужой код, вроде рабочий
    lname.send_keys('nanana')
    time.sleep(1)

    email = browser.find_element_by_class_name('third')
    email.send_keys('tututu@nanana.com')
    time.sleep(1)

    # block2
    phone = browser.find_element_by_xpath(
        '//input[@placeholder="Input your phone:"]')
    # phone = browser.find_elements_by_class_name('first')[-1]  # +
    phone.send_keys('223322223322')
    time.sleep(1)

    # address = browser.find_element_by_xpath(
    #     '//input[@placeholder="Input your address:"]')
    # address = browser.find_elements_by_class_name('second')[-1]  # +
    # address = browser.find_element_by_css_selector('.second_block .second_class .second')  # +
    address = browser.find_element_by_css_selector('div.second_block :nth-child(2) input.second')  # +
    address.send_keys('st Pushkina, apt Kolotushkina')
    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
