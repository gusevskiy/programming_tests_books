import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            executable_path="/home/gusevskiy/Documents/Dev/programming_tests_books/chromedriver/chromedriver_linux64/chromedriver"
        )

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get("http://localhost:8000")

        self.assertIn("To-Do", self.browser.title)

        # никогда не срабатывает и всегда генерирует переданное
        # сообщение об ошибке
        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main(warnings='ignore')