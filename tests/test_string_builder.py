import unittest
import allure
from app import app


@allure.feature('Тест конструктора строк')
class Test_string_builder(unittest.TestCase):
    def setUp(self) -> None:
        self.string_builder = app.String_builder()
    
    def test_add(self):
        self.string_builder.add_after("Hello")
        self.assertEqual(self.string_builder.add_after(", World!").build(), "Hello, World11!")

    def test_sub(self):
        self.string_builder.add_after("Hello")
        self.assertEqual(self.string_builder.add_before(", World!").build(), ", World!Hello")

if __name__ == "__main__":
    unittest.main()