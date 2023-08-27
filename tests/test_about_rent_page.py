import allure
from locators.locators import OrderPageLocators, AboutRentLocators
from data.urls import TestUrls
from pages.about_rent_page import AboutRentPage
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data.data import ExpectedText

@allure.feature('Проверка страницы "Про аренду". Сценарий заказа')
class TestAboutRentPage:

    @allure.title('Проверка перехода на главную страницу по клику на "Самокат" со страницы "Про аренду"')
    @allure.description('Нажать на логотип "Самоката", переход на главную страницу')
    def test_return_to_main_by_click_on_scooter_in_header(self, browser):
        OrderPage(browser).open_about_rent_page()
        about_rent_page = AboutRentPage(browser)
        about_rent_page.click_on_scooter_in_header()
        assert browser.current_url == TestUrls.MainPageUrl, 'Переход на главную страницу "Яндекс.Самокат" не осуществлен'

    @allure.title('Проверка перехода к форме заказа по клику на кнопку "назад"')
    @allure.description('Нажать кнопку "назад", переход к форме заказа')
    def test_click_on_back_button(self, browser):
        OrderPage(browser).open_about_rent_page()
        about_rent_page = AboutRentPage(browser)
        about_rent_page.click_on_back_button()
        assert about_rent_page.find_text(OrderPageLocators.HEADING_ON_ORDER_PAGE) == ExpectedText.heading_on_order_page, 'Переход к форме заказа не осуществлен'

    @allure.title('Проверка перехода на страницу подтверждения заказа')
    @allure.description('Заполнить поля формы "Про аренду", переход на страницу подтверждения заказа')
    def test_go_to_modal_window(self, browser):
        OrderPage(browser).open_about_rent_page()
        about_rent_page = AboutRentPage(browser)
        about_rent_page.go_to_confirmation_modal_window()
        assert about_rent_page.find_text(AboutRentLocators.HEADING_CONFIRMATION_MODAL).strip() == ExpectedText.heading_on_confirmation_modal, 'Переход на страницу подтверждения заказа не осуществлен'

    @allure.title('Проверка возврата на страницу "Про аренду" с окна подтверждения заказа')
    @allure.description('Заполнить поля "Про аренду", вернуться на страницу "Про аренду"')
    def test_return_to_about_rent_from_modal(self, browser):
        OrderPage(browser).open_about_rent_page()
        about_rent_page = AboutRentPage(browser)
        about_rent_page.click_no_button_on_confirmation_modal_window()
        assert about_rent_page.find_text(AboutRentLocators.HEADING_ON_ABOUT_PAGE) == ExpectedText.heading_about_rent, 'Переход на страницу "Про аренду" не осуществлен'

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в правом верхнем углу главной страницы')
    @allure.description('Нажать кнопку "Заказать" в правом верхнем углу страницы, заказать самокат')
    def test_order_confirmed_successfully_from_order_button_header(self, browser):
        main_page = MainPage(browser)
        order_page = OrderPage(browser)
        about_rent_page = AboutRentPage(browser)
        main_page.open_main_url()
        main_page.click_on_order_button_in_header()
        order_page.open_about_rent_page()
        about_rent_page.click_yes_button_on_confirmation_modal_window()
        assert about_rent_page.find_text(AboutRentLocators.LOOK_AT_STATUS) == ExpectedText.heading_look_at_status, 'Не удалось проверить статус заказа, поскольку номер заказа в урле ' \
                                                                                                                    'отсутствует либо не соответствует оформленному заказу'

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в нижней части главной страницы')
    @allure.description('Нажать кнопку "Заказать" в нижней части главной страницы, заказать самокат')
    def test_order_confirmed_successfully_from_order_button_body(self, browser):
        main_page = MainPage(browser)
        order_page = OrderPage(browser)
        about_rent_page = AboutRentPage(browser)
        main_page.open_main_url()
        main_page.click_on_order_button_in_body()
        order_page.open_about_rent_page()
        about_rent_page.click_yes_button_on_confirmation_modal_window()
        assert about_rent_page.find_text(AboutRentLocators.LOOK_AT_STATUS) == ExpectedText.heading_look_at_status, 'Статус заказа не проверен - номер заказа в URL отсутствует/не соответствует заказу'
