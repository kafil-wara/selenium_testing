from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# initialize the driver
driver = webdriver.Chrome()

# navigate to the application home page
driver.get("http://127.0.0.1:5000")

# test creating a new note
def test_create_note():
    # click on the new note button
    new_note_button = driver.find_element("xpath", '//a[@href="/new_note"]')
    new_note_button.click()
    time.sleep(1)

    # fill in the note form and submit
    title_input = driver.find_element("name", "title")
    body_input = driver.find_element("name", "content")
    title_input.send_keys("Test Note Title")
    body_input.send_keys("Test Note Body")
    submit_button = driver.find_element("name", "create")
    submit_button.click()
    time.sleep(1)
    # Take a screenshot of the page after creating the note
    driver.save_screenshot("notes.png")

    title_input = driver.find_elements(By.TAG_NAME, 'h2')[0]
    content_input = driver.find_element(By.TAG_NAME, 'p')
    
    print("\n")
    print("Title input from testing script: " + title_input.get_attribute("innerHTML"))
    print("Body input from testing script: " + content_input.get_attribute("innerHTML") + "\n")

    # Check that the title of the new note is correct
    assert title_input.get_attribute("innerHTML") == "Test Note Title"


# test editing an existing note
def test_edit_note():
    note_bodies = driver.find_elements(By.TAG_NAME, 'p')[0]
    print("Note body before updating: " + note_bodies.get_attribute("innerHTML"))
    # find an existing note and click the edit button
    edit_buttons = driver.find_elements(By.CLASS_NAME, "edit")
    
    edit_buttons[0].click()
    time.sleep(1)

    # update the note and submit
    body_input = driver.find_element("name", "content")
    body_input.clear()
    body_input.send_keys("Updated Note Body")
    submit_button = driver.find_element(By.CLASS_NAME, "editSub")
    submit_button.click()
    time.sleep(1)
    driver.save_screenshot("edits.png")

    # check that the note was updated and is displayed on the home page
    note_bodies = driver.find_elements(By.TAG_NAME, 'p')[0]
    print("Note body after updating: " + note_bodies.get_attribute("innerHTML") + "\n")
    assert note_bodies.get_attribute("innerHTML") == "Updated Note Body"
    

# test deleting an existing note
def test_delete_note():
    # find an existing note and click the delete button
    delete_buttons = driver.find_elements(By.CLASS_NAME, "dlt")
    delete_buttons[0].click()

    time.sleep(1)

    driver.save_screenshot("delete.png")

    # check that the note was deleted and is no longer displayed on the home page
    note_titles = driver.find_elements("class name", "card-title")
    note_titles_text = [title.text for title in note_titles]
    assert "Test Note Title" not in note_titles_text
    print("Deletion Successful\n")
    print("Completion Message: 3 tests ran, all tests successfuly completed")

# run the tests
test_create_note()
test_edit_note()
test_delete_note()



# close the driver
driver.close()
