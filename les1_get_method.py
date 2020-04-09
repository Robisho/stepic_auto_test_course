# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import time
from selenium import webdriver


url = 'https://stepik.org/lesson/25969/step/12'
driver = webdriver.Chrome()

time.sleep(5)

driver.get(url)  # открыли окно браузера по ссылке
time.sleep(5)

textarea = driver.find_element_by_css_selector('.textarea')  # нашли текстовое поле

textarea.send_keys('get()')  # в текстовом поле браузера написали текст
time.sleep(5)

submit_button = driver.find_element_by_css_selector('.submit-submission')
# жмакнули по кнопке отптавить
time.sleep(5)

driver.quit()  # закрыли браузер

class Dog(models.Model):
    """Model definition for Dog."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Dog."""

        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'

    def __str__(self):
        """Unicode representation of Dog."""
        pass

