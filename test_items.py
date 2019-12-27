import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_from(browser):
    browser.get(link)
    time.sleep(1)
    button = len(browser.find_elements_by_xpath("//form[@id='adds_to_basket_form']/button"))
    assert button > 0, 'Кнопка не найдена'
    
