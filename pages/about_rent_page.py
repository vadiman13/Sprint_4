import allure
from pages.base_page import BasePage
from data.data import Comments
from locators.locators import BasePageLocators, AboutRentLocators
from locators.locators import MainPaigeLocators, OrderPageLocators


class AboutRentPage(BasePage):

    @allure.step('Клик на логотип самоката')
    def click_on_scooter_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_SCOOTER_LOGO)
        self.find_element_located(MainPaigeLocators.MAIN_PAGE_HEADING)


    @allure.step('Клик на кнопку "Назад"')
    def click_on_back_button(self):
        self.click_on_element(AboutRentLocators.BACK_BUTTON)
        self.find_element_located(OrderPageLocators.HEADING_ON_ORDER_PAGE)


    @allure.step('Выбрать "Когда привезти самокат"')
    def choose_delivery_date(self):
        self.click_on_element(AboutRentLocators.DELIVERY_DATE_INPUT)
        self.click_on_element(AboutRentLocators.CHOSE_DATE)

    @allure.step('Выбрать срок аренды')
    def choose_rent_period(self):
        self.click_on_element(AboutRentLocators.RENTAL_PERIOD)
        self.click_on_element(AboutRentLocators.CHOSE_RENT_PERIOD)

    @allure.step('Выбрать цвет самоката')
    def choose_color(self):
        self.click_on_element(AboutRentLocators.BLACK_COLOR)

    @allure.step('Заполнить поле ввода "Комментарий для курьера"')
    def fill_comment_for_courier(self, comment=Comments.comments):
        self.add_value(AboutRentLocators.COMMENT_TO_COURIER_INPUT, comment)

    @allure.step('Нажать кнопку "Заказать", перейти на окно подтверждения')
    def go_to_confirmation_modal_window(self):
        self.choose_delivery_date()
        self.choose_rent_period()
        self.choose_color()
        self.fill_comment_for_courier()
        self.click_on_element(AboutRentLocators.BODY_ORDER_BUTTON)
        self.find_element_located(AboutRentLocators.YES_BUTTON_MODAL)

    @allure.step('Нажать кнопку "Нет" в окне подтверждения заказа')
    def click_no_button_on_confirmation_modal_window(self):
        self.go_to_confirmation_modal_window()
        self.click_on_element(AboutRentLocators.NO_BUTTON_MODAL)
        self.find_element_located(AboutRentLocators.BODY_ORDER_BUTTON)

    @allure.step('Нажать кнопку "Да" в окне подтверждения заказа')
    def click_yes_button_on_confirmation_modal_window(self):
        self.go_to_confirmation_modal_window()
        self.click_on_element(AboutRentLocators.YES_BUTTON_MODAL)
        self.find_element_located(AboutRentLocators.LOOK_AT_STATUS)
