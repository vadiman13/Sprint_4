import time

import allure
from locators.locators import OrderPageLocators, AboutRentLocators
from pages.order_page import OrderPage
from data.data import ExpectedText as ExT


@allure.feature('Проверка страницы "Для кого самокат" ')
class TestOrderPage:

    @allure.title('Проверка перехода на страницу "Про аренду" по клику на кнопку "Далее" после успешного заполнения клиентскими данными')
    @allure.description('Заполнить форму, перейти на страницу "Про аренду"')
    def test_fill_client_info_succsesfully(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.fill_client_info()
        order_page.fill_metro_field_by_click()
        order_page.click_on_button_forward()
        assert order_page.find_text(AboutRentLocators.HEADING_ON_ABOUT_PAGE) == ExT.heading_about_rent, 'Переход на страницу "Про аренду" про аренду не осуществлен'

    @allure.title('Проверка валидации поля "Имя"')
    @allure.description('Поле "Имя" не заполнено')
    def test_validate_error_by_input_first_name(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error()
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_FIRST_NAME) == ExT.messege_validate_first_name,  'Не отображена ошибка валидации'

    @allure.title('Проверка валидации поля "Фамилия"')
    @allure.description('Поле "Фамилия" не заполнено')
    def test_validate_error_by_input_second_name(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error()
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_SECOND_NAME) == ExT.messege_validate_second_name,  'Не отображена ошибка валидации'

    @allure.title('Проверка валидации поля "Адрес: куда привезти заказ"')
    @allure.description('Поле "Адрес: куда привезти заказ" заполнено некорректно')
    def test_validate_error_by_input_delivery_address(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.fill_adress_invalid_value()
        order_page.click_on_button_forward_for_validate_error()
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_DELIVERY_ADDRESS) == ExT.messege_validate_delivery_address,  'Не отображена ошибка валидации'

    @allure.title('Проверка валидации поля "Станция метро"')
    @allure.description('Пропустить выбор станции')
    def test_validate_error_by_input_metro_station(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error()
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_METRO_STATION) == ExT.messege_validate_metro_station, 'Не отображена ошибка валидации'



    @allure.title('Проверка валидации поля "Номера телефона"')
    @allure.description('Поле "Номера телефона" не заполнено')
    def test_validate_error_by_input_phone_number(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error()
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_PHONE_NUMBER) == ExT.messege_validate_phone_number, 'Не отображена ошибка валидации'