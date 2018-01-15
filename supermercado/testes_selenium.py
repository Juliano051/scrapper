import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get("https://medium.com/")
time.sleep(1)

elem = driver.find_element_by_tag_name("body")

no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -= 1

post_elem = driver.find_elements_by_class_name("ui-summary")

for post in post_elem:
    print(post.text)
