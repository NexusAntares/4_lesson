import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("reg_email").send_keys("VasiliyPupkin@bk.ru")
driver.find_element_by_id("reg_password").send_keys("fglEggl32LFSJL443dfsvfds")
time.sleep(1)
driver.find_element_by_name("register").click()


driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("VasiliyPupkin@bk.ru")
driver.find_element_by_id("password").send_keys("fglEggl32LFSJL443dfsvfds")
time.sleep(1)
driver.find_element_by_name("login").click()
time.sleep(5)
driver.quit()