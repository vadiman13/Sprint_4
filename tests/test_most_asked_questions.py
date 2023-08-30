import allure
import pytest
from data.data import Answers
from pages.main_page import MainPage

@allure.feature('Вопросы о важном')
class TestMostAskedQuestions:
    @allure.title('Проверка блока вопросов')
    @allure.description('Проверка соответствия вопросов и ответов')
    @pytest.mark.parametrize("index", range(8))
    def test_click_on_questions(self, browser, index):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.scroll_to_question_section()
        main_page.click_on_question(index)
        answer = main_page.get_answers()
        assert answer == Answers.answers[index], f'Неверный ответ. Ожидалось: {Answers.answers[index]}'
