from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import unittest

class NewVisitorTest(LiveServerTestCase):
    '''тест нового поситителя'''
    
    MAX_WAIT: int = 10
    
    def setUp(self) -> None:
        '''установка'''
        self.browser = webdriver.Firefox()
        
    def tearDown(self) -> None:
        '''демонтаж'''
        self.browser.quit()
        
    def wait_for_row_in_list_table(self, row_text):
        '''ожидать строку в таблице списка'''
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > self.MAX_WAIT:
                    raise e
                time.sleep(0.5)
        
            
    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        # Эдит слышала про крутое новое онлайн-приложение со списком
        # неотложных дел. Она решает оценить его домашнюю страницу
        self.browser.get(self.live_server_url)
        # Она видит, что заголовок и шапка страницы говорят о списках
        # неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)
        # Ей сразу же предлагается ввести элемент списка
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # Она набирает в текстовом поле "Купить павлиньи перья"
        # (ее хобби – вязание рыболовных мушек)
        inputbox.send_keys('Купить павлиньи перья')
        # Когда она нажимает enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')
        # Текствое поле по-прежнему приглашает ее добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        # (Эдит очень методична)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)
        # Страница снова обновляется и теперь показывает оба элемента ее списка
        self.wait_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')
        # Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
        # сайт сгенерировал для нее уникальный URL-адрес – об этом
        # выводится небольшой текст с пояснениями.
        self.fail('Закончить тест!')
        # Она посещает этот URL-адрес – ее список по-прежнему там.
        
    # def test_multiple_users_can_start_lists_at_different_urls(self):
    #     '''тест: многочисленные пользователи могут начать списки по разным url'''
    #     # Эдит начинает новый список
    #     self.browser.get(self.live_server_url)
    #     inputbox = self.browser.find_element(By.ID, 'id_new_item')
    #     inputbox.send_keys('Купить павлиньи перья')
    #     inputbox.send_keys(Keys.ENTER)
    #     self.wait_for_row_in_list_table('1: Купить павлиньи перья')
    #     # Она замечает, что ее список имеет уникальный URL-адрес
    #     edith_list_url = self.browser.current_url
    #     self.assertRegex(edith_list_url, '/lists/.+')
        
    #     # Теперь новый пользователь, Фрэнсис, приходит на сайт.
    #     ## Мы используем новый сеанс браузера, тем самым обеспечивая, чтобы никакая
    #     ## информация от Эдит не прошла через данные cookie и пр.
    #     self.browser.quit()
    #     self.browser = webdriver.Firefox()
    #     # Фрэнсис посещает домашнюю страницу. Нет никаких признаков списка Эдит
    #     self.browser.get(self.live_server_url)
    #     page_text = self.browser.find_element(By.TAG_NAME, 'body').text
    #     self.assertNotIn('Купить павлиньи перья', page_text)
    #     self.assertNotIn('Сделать мушку', page_text)
        
    #     # Фрэнсис начинает новый список, вводя новый элемент. Он менее
    #     # интересен, чем список Эдит...
    #     inputbox = self.browser.find_element(By.ID, 'id_new_item')
    #     inputbox.send_keys('Купить молоко')
    #     inputbox.send_keys(Keys.ENTER)
    #     self.wait_for_row_in_list_table('1: Купить молоко')
        
    #     # Фрэнсис получает уникальный URL-адрес
    #     francis_list_url = self.browser.current_url
    #     self.assertRegex(francis_list_url, '/lists/.+')
    #     self.assertNotEqual(francis_list_url, edith_list_url)
    #     # Опять-таки, нет ни следа от списка Эдит
    #     page_text = self.browser.find_element(By.TAG_NAME, 'body').text
    #     self.assertNotIn('Купить павлиньи перья', page_text)
    #     self.assertIn('Купить молоко', page_text)
            
if __name__ == '__main__':
    unittest.main()