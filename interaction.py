from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.WEBSITENAME.com")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("XXXX")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("YYYY")
email = driver.find_element_by_name("email")
email.send_keys(XXXX@email.com)

submit = driver.find_by_css_selector("form button")
submit.click()





