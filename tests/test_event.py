import unittest
from colorama import Fore
from uuid import UUID, uuid4
from app import Event, Owner


class TestEvent(unittest.TestCase):
    def setUp(self) -> None:
        self.uuid_owner = uuid4()
        self.uuid_event = uuid4()
        self.owner_data = {
            "uuid": self.uuid_owner.bytes,
            "name": "John Doe"
        }
        self.event_test_data = {
            "uuid": self.uuid_event.bytes,
            "description": "This is a test event",
            "event_type": "test",
            "createdAt": "2020-01-01T00:00:00.000Z",
            "creator": self.owner_data
        }

    def test_instance(self):
        event = Event(self.event_test_data)
        self.assertTrue(type(event) is Event)

    def test_to_json(self):
        event = Event(self.event_test_data)
        expected = {
            "id": str(self.uuid_event),
            "description": "This is a test event",
            "event_type": "test",
            "createdAt": "2020-01-01T00:00:00.000Z",
            "creator": Owner(self.owner_data).__to_json__()
        }
        self.assertEqual(event.__to_json__(), expected)

    def test_raise_exception_if_data_missing(self):
        data_event = {
            "uuid": None,
            "description": "This is a test event",
            "event_type": "test",
            "createdAt": "2020-01-01T00:00:00.000Z",
            "creator": self.owner_data
        }
        with self.assertRaises(Exception):
            Event(data_event)

        data_event = {
            "uuid": self.uuid_event.bytes,
            "description": None,
            "event_type": "test",
            "createdAt": "2020-01-01T00:00:00.000Z",
            "creator": self.owner_data
        }
        with self.assertRaises(Exception):
            Event(data_event)

        data_event = {
            "uuid": self.uuid_event.bytes,
            "description": "This is a test event",
            "event_type": None,
            "createdAt": "2020-01-01T00:00:00.000Z",
            "creator": self.owner_data
        }
        with self.assertRaises(Exception):
            Event(data_event)

        data_event = {
            "uuid": self.uuid_event.bytes,
            "description": "This is a test event",
            "event_type": "test",
            "createdAt": None,
            "creator": self.owner_data
        }
        with self.assertRaises(Exception):
            Event(data_event)

        data_event = {
            "uuid": self.uuid_event.bytes,
            "description": "This is a test event",
            "event_type": "test",
            "createdAt": "2020-01-01T00:00:00.000Z",
            "creator": None
        }
        with self.assertRaises(Exception):
            Event(data_event)

        data_event = {
            "uuid": None,
            "description": None,
            "event_type": None,
            "createdAt": None,
            "creator": None
        }
        with self.assertRaises(Exception):
            Event(data_event)

    def test_raise_exception_if_data_type_is_wrong(self):
        data_event = {
            "uuid": "this is not a uuid",
            "description": "This is a test event",
            "event_type": "test",
            "createdAt": "2020-01-01T00:00:00.000Z",
            "creator": self.owner_data
        }
        with self.assertRaises(Exception):
            Event(data_event)

        data_event = {
            "uuid": self.uuid_event.bytes,
            "description": "This is a test event",
            "event_type": 123,
            "createdAt": "2020-01-01T00:00:00.000Z",
            "creator": self.owner_data
        }
        with self.assertRaises(Exception):
            Event(data_event)

        data_event = {
            "uuid": self.uuid_event.bytes,
            "description": "This is a test event",
            "event_type": "test",
            "createdAt": 123,
            "creator": self.owner_data
        }
        with self.assertRaises(Exception):
            Event(data_event)

        data_event = {
            "uuid": self.uuid_event.bytes,
            "description": "This is a test event",
            "event_type": "test",
            "createdAt": "2020-01-01T00:00:00.000Z",
            "creator": "this is not a owner"
        }
        with self.assertRaises(Exception):
            Event(data_event)

        data_event = {
            "uuid": "this is not a uuid",
            "description": 123,
            "event_type": 123,
            "createdAt": 123,
            "creator": "this is not a owner"
        }
        with self.assertRaises(Exception):
            Event(data_event)

    def test_raise_exception_if_data_is_empty(self):
        with self.assertRaises(Exception):
            Event({})

    @classmethod
    def tearDownClass(cls):
        print(Fore.YELLOW + ">>>>>> End of Event tests" + Fore.RESET)

    @classmethod
    def setUpClass(cls):
        print(Fore.GREEN + ">>>>>> Start of Event tests" + Fore.RESET)