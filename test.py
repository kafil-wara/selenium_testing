from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

    # check that the note was created and is displayed on the home page
    # note_titles = driver.find_elements("class name", "card-title")
    # note_titles_text = [title.text for title in note_titles]
    # assert "Test Note Title" in note_titles_text


    # Check that the title of the new note is correct
    #time.sleep(2)

    title_input = driver.find_elements(By.TAG_NAME, 'h2')[0]
    #time.sleep(2)

    print(title_input.get_attribute("innerHTML"))

    assert title_input.get_attribute("innerHTML") == "Test Note Title"


# test editing an existing note
def test_edit_note():
    # find an existing note and click the edit button
    edit_buttons = driver.find_elements(By.CLASS_NAME, "editSub")
    edit_buttons.click()
    time.sleep(1)

    # update the note and submit
    body_input = driver.find_element("name", "content")
    body_input.clear()
    body_input.send_keys("Updated Note Body")
    submit_button = driver.find_element("name", "create")
    submit_button.click()
    time.sleep(1)

    # check that the note was updated and is displayed on the home page
    note_bodies = driver.find_elements("class name", "card-text")
    note_bodies_text = [body.text for body in note_bodies]
    assert "Updated Note Body" in note_bodies_text

# test deleting an existing note
def test_delete_note():
    # find an existing note and click the delete button
    delete_buttons = driver.find_elements("class name", "btn-danger")
    delete_buttons[0].click()
    time.sleep(1)

    # accept the confirmation dialog
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)

    # check that the note was deleted and is no longer displayed on the home page
    note_titles = driver.find_elements("class name", "card-title")
    note_titles_text = [title.text for title in note_titles]
    assert "Test Note Title" not in note_titles_text

# run the tests
test_create_note()
test_edit_note()
test_delete_note()

# close the driver
driver.close()
