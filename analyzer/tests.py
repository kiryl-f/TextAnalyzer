from django.test import TestCase
from .views import average_word_count
from .models import Text

class AnalyzerTests(TestCase):

    def test_word_counter(self):
        text \
            = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        self.assertIs(average_word_count(text), 14)

    def test_text_model(self):
        text = Text(title='Title', text='Text')
        self.assertEqual(text.title, 'Title')
