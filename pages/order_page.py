import allure
from pages.base_page import BasePage
from locators.locators import OrderPageLocators, AboutRentLocators
from data.urls import TestUrls
from data.generators import GeneratedData
from data.data import InvalidAdress


class OrderPage(BasePage):

    @allure.step('Открыть страницу заказа')
    def open_order_url(self):
        self.open_start_url(TestUrls.OrderPageUrl)


    @allure.step('Кликнуть на кнопку "Далее"')
    def click_on_button_forward(self):
        self.click_on_element(OrderPageLocators.ORDER_CONTINUE_BUTTON)
        self.find_element_located(AboutRentLocators.HEADING_ON_ABOUT_PAGE)

    @allure.step('Нажать кнопку "Далее" без заполнения формы ')
    def click_on_button_forward_for_validate_error(self):
        self.click_on_element(OrderPageLocators.ORDER_CONTINUE_BUTTON)
        self.find_element_located(OrderPageLocators.VALIDATE_ERROR_FIRST_NAME)

    @allure.step('Заполнить поле "Адрес: куда привезти заказ" невалидным значением')
    def fill_adress_invalid_value(self, invalid_delivery_address=InvalidAdress.invalid_delivery_address):
        self.add_value(OrderPageLocators.DELIVERY_ADDRESS_INPUT, invalid_delivery_address)

    @allure.step('Заполнить форму "Для кого самокат"')
    def fill_client_info(self, first_name=GeneratedData.generate_first_name(),
                         last_name=GeneratedData.generate_last_name(),
                         delivery_address=GeneratedData.generate_delivery_address(),
                         phone_number=GeneratedData.generate_phone_number()):

        self.add_value(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.add_value(OrderPageLocators.SECOND_NAME_INPUT, last_name)
        self.add_value(OrderPageLocators.DELIVERY_ADDRESS_INPUT, delivery_address)
        self.add_value(OrderPageLocators.PHONE_NUMBER_INPUT, phone_number)

    @allure.step('Выбрать станцию метро')
    def fill_metro_field_by_click(self):
        self.click_on_element(OrderPageLocators.METRO_STATION_INPUT)
        self.click_on_element(OrderPageLocators.METRO_STATION_FOR_CLICK)

    @allure.step('Перейти на страницу "Про аренду"')
    def open_about_rent_page(self):
        self.open_order_url()
        self.fill_client_info()
        self.fill_metro_field_by_click()
        self.click_on_button_forward()
