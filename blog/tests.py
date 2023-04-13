from time import sleep

from django.test import TestCase
from selenium import webdriver


class SeleniumTest(TestCase):
    def test_one(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/blog/")
        driver.find_element_by_link_text('Создать блог').click()

        name = driver.find_element_by_name('name')
        name.send_keys('Тестовое имя')

        location = driver.find_element_by_name('title')
        location.send_keys('Тестовая запись')

        discription = driver.find_element_by_name('description')
        discription.send_keys('Тестовое описание блога')

        button = driver.find_element_by_xpath("//*[contains(text(), 'Сохранить')]")
        button.click()

        sleep(10)

        driver.close()


class BlogTestCase(TestCase):
    def test_open_blog_edit(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/")
