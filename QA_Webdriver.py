import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://prom.ua")

Search_header = "холодильник"
expected_text = "«холодильник»\nв Украине"
time.sleep(4)
browser.find_element_by_css_selector('[name="search_term"]').send_keys(Search_header)
time.sleep(15)
browser.find_element_by_css_selector('[name="search_term"]').send_keys(Keys.RETURN)
time.sleep(15)
current_text = browser.find_element_by_css_selector('h1.ek-text').text


assert current_text == expected_text
time.sleep(4)

