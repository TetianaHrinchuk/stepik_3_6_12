from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    try:
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        result = True
    except:
        result = False
    assert result == True, "No button"
    