from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_test_method_1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    driver.maximize_window ()
