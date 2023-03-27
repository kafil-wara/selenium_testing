from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the home page and verify that it loads successfully
driver.get("http://localhost:5000")
assert "Notes App" in driver.title

# Navigate to the create note page and verify that it loads successfully
driver.find_element_by_link_text("New Note").click()
assert "New Note" in driver.title

# Create a new note and verify that it is created successfully
title_field = driver.find_element_by_name("title")
content_field = driver.find_element_by_name("content")
title_field.send_keys("Test Note Title")
content_field.send_keys("This is a test note.")
driver.find_element_by_css_selector(".btn-primary").click()
assert "Test Note Title" in driver.page_source

# Navigate to the edit note page and verify that it loads successfully
driver.find_element_by_link_text("Edit").click()
assert "Edit Note" in driver.title

# Edit the existing note and verify that the changes are saved successfully
title_field.clear()
content_field.clear()
title_field.send_keys("Edited Note Title")
content_field.send_keys("This is an edited note.")
driver.find_element_by_css_selector(".btn-primary").click()
assert "Edited Note Title" in driver.page_source

# Navigate to the delete note page and verify that it loads successfully
driver.find_element_by_link_text("Delete").click()
assert "Delete Note" in driver.title

# Delete the existing note and verify that it is deleted successfully
driver.find_element_by_css_selector(".btn-danger").click()
WebDriverWait(driver, 10).until(EC.title_contains("Notes App"))
assert "Edited Note Title" not in driver.page_source

# Close the browser window
driver.quit()
