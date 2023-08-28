import allure
from pages.base_page import BasePage
from locators.locators import BasePageLocators, MainPaigeLocators, OrderPageLocators
from data.urls import TestUrls




class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open_main_url(self):
        self.open_start_url(TestUrls.MainPageUrl)

    @allure.step('Закрыть окно cookie')
    def close_cookie(self):
        self.accept_cookie(BasePageLocators.ACCEPT_COOKIE_BUTTON)
        self.find_element_not_located(BasePageLocators.COOKIE)


    @allure.step('Нажать на логотип в шапке')
    def click_yandex_logo_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_YANDEX_LOGO)
        self.switch_to_new_window()
        self.find_element_located(MainPaigeLocators.DZEN_LOGO)


    @allure.step('Cokies закрыты')
    def is_cookie_not_visible(self):
        return self.find_element_not_located(BasePageLocators.COOKIE)

    @allure.step('Нажать логотип самоката в шапке')
    def click_on_scooter_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_SCOOTER_LOGO)

    @allure.step('Нажать кнопку "Заказать" в шапке')
    def click_on_order_button_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_ORDER_BUTTON)
        self.find_element_located(OrderPageLocators.HEADING_ON_ORDER_PAGE)

    @allure.step('Скролл до кнопки заказать в body')
    def scroll_to_order_button_in_body(self):
        self.close_cookie()
        self.scroll_to(MainPaigeLocators.BODY_ORDER_BUTTON)
        self.find_element_located(MainPaigeLocators.BODY_ORDER_BUTTON)
        self.find_element_clickable(MainPaigeLocators.BODY_ORDER_BUTTON)

    @allure.step('Скролл до кнопки "Заказать" в body')
    def click_on_order_button_in_body(self):
        self.scroll_to_order_button_in_body()
        self.click_on_element(MainPaigeLocators.BODY_ORDER_BUTTON)
        self.find_element_located(OrderPageLocators.HEADING_ON_ORDER_PAGE)


    @allure.step('Скролл до секции вопросов')
    def scroll_to_question_section(self):
        self.scroll_to(MainPaigeLocators.QUESTION_SECTION)

    @allure.step('Нажать на вопрос')
    def click_on_question(self, index):
        self.wait_element_visible(MainPaigeLocators.QUESTION_SECTION)
        questions = self.find_elements_located(MainPaigeLocators.QUESTION)
        questions[index].click()

    @allure.step('Проверить ответ')
    def get_answers(self):
        self.wait_element_visible(MainPaigeLocators.ANSWER)
        return self.find_element_located(MainPaigeLocators.ANSWER).text
