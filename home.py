import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 .button").click()
driver.find_element_by_css_selector(".tabs li:nth-child(2)").click()
driver.find_element_by_css_selector(".star-5").click()
driver.find_element_by_id("comment").send_keys("Nice book!")
driver.find_element_by_id("author").send_keys("VasiliyPupkin")
driver.find_element_by_id("email").send_keys("VasiliyPupkin@bk.ru")
driver.find_element_by_name("submit").click()



time.sleep(5)
driver.quit()