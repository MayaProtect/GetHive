import unittest
from colorama import Fore
from app import app


class TestApp(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        print(Fore.YELLOW + ">>>>>> End of App tests" + Fore.RESET)

    @classmethod
    def setUpClass(cls):
        print(Fore.GREEN + ">>>>>> Start of App tests" + Fore.RESET)
