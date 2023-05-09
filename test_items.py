import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
def test_check__basket_button(browser, link):
    """Проверка наличия кнопки 'Добавить в корзину' на странице"""
    browser.get(link)
    browser.implicitly_wait(10)
    # Найти и нажать кнопку "Добавить в корзину"
    browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')

