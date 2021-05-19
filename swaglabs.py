from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(r"C:\Users\APURAV\PycharmProjects\selenium test\Browsers\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
driver.find_element_by_id("user-name").send_keys("standard_user")
time.sleep(1)

driver.find_element_by_id("password").send_keys("secret_sauce")
time.sleep(1)

driver.find_element_by_name("login-button").send_keys(Keys.ENTER)
time.sleep(1)

driver.find_element_by_name("add-to-cart-sauce-labs-bolt-t-shirt").send_keys(Keys.ENTER)
time.sleep(5)

driver.find_element_by_id("shopping_cart_container").click()
time.sleep(1)
driver.find_element_by_id("checkout").click()

time.sleep(1)

driver.find_element_by_id("first-name").send_keys("Utsav")
time.sleep(1)

driver.find_element_by_id("last-name").send_keys("Sharma")
time.sleep(1)

driver.find_element_by_id("postal-code").send_keys("245101")
time.sleep(1)
driver.find_element_by_id("continue").click()
time.sleep(2)
driver.find_element_by_id("finish").click()
time.sleep(2)
driver.find_element_by_id("react-burger-menu-btn").click()
time.sleep(2)
driver.find_element_by_id("logout_sidebar_link").click()









