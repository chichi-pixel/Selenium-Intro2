from selenium import webdriver

from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("articlecount")
print(article_count.text)
article_count.click()

all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Berlin")
search.send_keys(selenium.webdriver.Keys.ENTER)

#search = driver.find_element_by_name("search").send_keys("Berlin" + Keys.RETURN)