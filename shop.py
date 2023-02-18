import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("VasiliyPupkin@bk.ru")
driver.find_element_by_id("password").send_keys("fglEggl32LFSJL443dfsvfds")
driver.find_element_by_name("login").click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector("[data-product_id='181']").click()
book_title = driver.find_element_by_css_selector("h1.product_title")
title_text = book_title.text
assert title_text == "HTML5 Forms"
time.sleep(5)
driver.quit()


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("VasiliyPupkin@bk.ru")
driver.find_element_by_id("password").send_keys("fglEggl32LFSJL443dfsvfds")
driver.find_element_by_name("login").click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector(".cat-item-19").click()
items_count = driver.find_elements_by_css_selector(".product_cat-html.product_tag-html")
assert len(items_count) == 3
time.sleep(5)
driver.quit()


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("VasiliyPupkin@bk.ru")
driver.find_element_by_id("password").send_keys("fglEggl32LFSJL443dfsvfds")
driver.find_element_by_name("login").click()
driver.find_element_by_id("menu-item-40").click()
selector_def_sort_check =  driver.find_element_by_css_selector(".orderby [selected='selected']")
check_value = selector_def_sort_check.get_attribute("value")
assert check_value == "menu_order"
sortby_desc = driver.find_element_by_css_selector(".orderby")
select = Select(sortby_desc)
select.select_by_value("price-desc")
# select.select_by_index(5)
selector_check = driver.find_element_by_css_selector(".orderby [selected='selected']")
element_get_text = selector_check.text
assert element_get_text == "Sort by price: high to low"

time.sleep(5)
driver.quit()


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("VasiliyPupkin@bk.ru")
driver.find_element_by_id("password").send_keys("fglEggl32LFSJL443dfsvfds")
driver.find_element_by_name("login").click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector(".products.masonry-done li:nth-child(1)").click()
old_price_test = driver.find_element_by_css_selector("del span.amount")
old_price_text = old_price_test.text
assert old_price_text == "₹600.00"
new_price_test = driver.find_element_by_css_selector("ins span.amount")
new_price_text = new_price_test.text
assert new_price_text == "₹450.00"
wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-main-image")) ).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) ).click()

time.sleep(5)
driver.quit()

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("VasiliyPupkin@bk.ru")
driver.find_element_by_id("password").send_keys("fglEggl32LFSJL443dfsvfds")
driver.find_element_by_name("login").click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector(".products.masonry-done li:nth-child(6)").click()
driver.find_element_by_class_name("single_add_to_cart_button").click()
cart_test = driver.find_element_by_css_selector("span.cartcontents")
cart_text = cart_test.text
assert cart_text == "1 Item"
cart_test = driver.find_element_by_css_selector("span.amount")
cart_text = cart_test.text
assert cart_text == "₹350.00"
driver.find_element_by_id("wpmenucartli").click()
wait = WebDriverWait(driver, 20)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart_totals  tr:nth-child(1) .amount"), "₹350.00"))
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart_totals  tr:nth-child(3) .amount"), "₹357.00"))

time.sleep(5)
driver.quit()



driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("VasiliyPupkin@bk.ru")
driver.find_element_by_id("password").send_keys("fglEggl32LFSJL443dfsvfds")
driver.find_element_by_name("login").click()
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector(".products.masonry-done li:nth-child(6)").click()
driver.find_element_by_class_name("single_add_to_cart_button").click()
driver.find_element_by_id("wpmenucartli").click()
quantity_change = driver.find_element_by_css_selector(".quantity input")
quantity_change.clear()
quantity_change.send_keys(3)
driver.find_element_by_css_selector("[value='Update Basket']").click()
time.sleep(2)
driver.find_element_by_css_selector("[value='Apply Coupon']").click()
wait = WebDriverWait(driver, 20)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code."))

time.sleep(5)
driver.quit()


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("VasiliyPupkin@bk.ru")
driver.find_element_by_id("password").send_keys("fglEggl32LFSJL443dfsvfds")
driver.find_element_by_name("login").click()
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector(".products.masonry-done li:nth-child(6)").click()
driver.find_element_by_class_name("single_add_to_cart_button").click()
driver.find_element_by_id("wpmenucartli").click()
wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout a")) ).click()
wait.until(EC.element_to_be_clickable((By.ID, "billing_first_name")) ).send_keys("Vasiliy")
driver.find_element_by_id("billing_last_name").send_keys("Pupkin")
driver.find_element_by_id("billing_email").send_keys("VasiliyPupkin@bk.ru")
driver.find_element_by_id("billing_phone").send_keys("15551234")
driver.find_element_by_id("s2id_billing_country").click()
time.sleep(1)
driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
time.sleep(1)
driver.find_element_by_css_selector("ul.select2-results").click()
driver.find_element_by_id("billing_address_1").send_keys("Pupkinskaya street, 69")
driver.find_element_by_id("billing_city").send_keys("Pupkinsk")
driver.find_element_by_id("billing_state").send_keys("Pupkinskaya oblast")
driver.find_element_by_id("billing_postcode").send_keys("123456")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
driver.find_element_by_id("payment_method_cheque").click()
driver.find_element_by_id("place_order").click()
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method strong"), "Check Payments"))