from selenium import webdriver

from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://9to5google.com/2022/09/08/google-fi-iphone-wi-fi-calling/")

currently_reading = driver.find_element_by_css_selector("currently-reading")
print(currently_reading.text)
article_count.click()

all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Google Fi")
search.send_keys(selenium.webdriver.Keys.ENTER)

#search = driver.find_element_by_name("search").send_keys("Google Fi" + Keys.RETURN)