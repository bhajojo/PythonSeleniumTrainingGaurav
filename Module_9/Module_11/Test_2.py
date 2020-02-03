import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def test_something():
    binary = FirefoxBinary("C://Program Files//Mozilla Firefox//firefox.exe")
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    driver.maximize_window()
