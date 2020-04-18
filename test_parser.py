import unittest
import pytest
from .main import quiz, search, recursive_search
from .keys  import ROOT_URL_YA

class user_answers_test(unittest.TestCase):

    def test_null_answers(self):
        res = ''
        self.assertEqual(res, '')

    def no_keys(self):
        res = ROOT_URL_YA
        self.assertEqual(res, 'https://yandex.ru/search/?')




if __name__ == '__main__':
    user_answers_test
