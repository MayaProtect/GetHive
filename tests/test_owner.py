import unittest

from colorama import Fore
from uuid import UUID, uuid4
from app import Owner


class TestOwner(unittest.TestCase):
    def setUp(self) -> None:
        self.uuid_owner = uuid4()
        self.owner_test_data = {
            "uuid": self.uuid_owner.bytes,
            "name": "John Doe"
        }

    def test_raise_exception_if_data_missing(self):
        owner_data = {
            "uuid": None,
            "name": "John Doe"
        }
        with self.assertRaises(Exception):
            Owner(owner_data)

        owner_data = {
            "uuid": self.uuid_owner,
            "name": None
        }
        with self.assertRaises(Exception):
            Owner(owner_data)

        owner_data = {
            "uuid": None,
            "name": None
        }
        with self.assertRaises(Exception):
            Owner(owner_data)

    def test_raise_exception_if_data_type_is_wrong(self):
        owner_data = {
            "uuid": "wrong type",
            "name": "John Doe"
        }
        with self.assertRaises(Exception):
            Owner(owner_data)

        owner_data = {
            "uuid": self.uuid_owner,
            "name": 123
        }
        with self.assertRaises(Exception):
            Owner(owner_data)

        owner_data = {
            "uuid": 123,
            "name": 123
        }
        with self.assertRaises(Exception):
            Owner(owner_data)

    def test_instance(self):
        owner = Owner(self.owner_test_data)
        self.assertTrue(type(owner) is Owner)

    def test_to_json(self):
        owner = Owner(self.owner_test_data)
        expected = {
            "id": str(self.uuid_owner),
            "name": "John Doe"
        }
        self.assertEqual(owner.__to_json__(), expected)

    @classmethod
    def tearDownClass(cls):
        print(Fore.YELLOW + ">>>>>> End of Owner tests" + Fore.RESET)

    @classmethod
    def setUpClass(cls):
        print(Fore.GREEN + ">>>>>> Start of Owner tests" + Fore.RESET)