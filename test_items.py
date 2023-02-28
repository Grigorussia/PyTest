#  import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language_transmission(browser):
    browser.get(link)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket_button.is_displayed(), "Кнопка добавления товара в корзину отсутствует"
#  time.sleep(30) #  Please turn on for check "fr"