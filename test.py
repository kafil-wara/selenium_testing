from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://localhost:5000/")

assert "Notes App" in driver.title

elem = driver.find_element_by_name("search")
elem.clear()
elem.send_keys("note")

elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source

driver.find_element_by_xpath('//a[text()="New Note"]').click()

assert "New Note" in driver.title

driver.find_element_by_name("title").send_keys("Test Note")
driver.find_element_by_name("content").send_keys("This is a test note.")

driver.find_element_by_name("submit").click()

assert "Test Note" in driver.page_source

driver.quit()
