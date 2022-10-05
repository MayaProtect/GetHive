import unittest
from colorama import Fore
from uuid import UUID, uuid4
from app import Hive


class TestHive(unittest.TestCase):
    def setUp(self) -> None:
        self.uuid_hive = uuid4()
        self.uuid_station = uuid4()
        self.uuid_owner = uuid4()
        self.event1_uuid = uuid4()
        self.event2_uuid = uuid4()
        self.hive_test_data = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": {
                "uuid": self.uuid_owner.bytes,
                "name": "John Doe"
            },
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": [
                {
                    "uuid": self.event1_uuid.bytes,
                    "description": "This is a test event",
                    "event_type": "test",
                    "createdAt": "2020-01-01T00:00:00.000Z",
                    "creator": {
                        "uuid": self.uuid_owner.bytes,
                        "name": "John Doe"
                    }
                },
                {
                    "uuid": self.event2_uuid.bytes,
                    "description": "This is a test event",
                    "event_type": "test",
                    "createdAt": "2020-01-01T00:00:00.000Z",
                    "creator": {
                        "uuid": self.uuid_owner.bytes,
                        "name": "John Doe"
                    }
                }
            ]
        }
        self.maxDiff = None

    def test_instance(self):
        hive = Hive(self.hive_test_data)
        self.assertTrue(type(hive) is Hive)

    def test_to_json(self):
        expected = {
            "id": str(self.uuid_hive),
            "station": str(self.uuid_station),
            "owner": {
                "id": str(self.uuid_owner),
                "name": "John Doe"
            },
            "last_temperature": 20.0,
            "last_sound_level": 67.3,
            "last_weight": 37.5,
            "last_events": [
                {
                    "id": str(self.event1_uuid),
                    "description": "This is a test event",
                    "event_type": "test",
                    "createdAt": "2020-01-01T00:00:00.000Z",
                    "creator": {
                        "id": str(self.uuid_owner),
                        "name": "John Doe"
                    }
                },
                {
                    "id": str(self.event2_uuid),
                    "description": "This is a test event",
                    "event_type": "test",
                    "createdAt": "2020-01-01T00:00:00.000Z",
                    "creator": {
                        "id": str(self.uuid_owner),
                        "name": "John Doe"
                    }
                }
            ]
        }
        hive = Hive(self.hive_test_data)
        self.assertEqual(hive.__to_json__(), expected)

    def test_raise_exception_if_data_missing(self):
        owner_data = {
            "uuid": self.uuid_owner.bytes,
            "name": "John Doe"
        }

        events_data = [
            {
                "uuid": self.event1_uuid.bytes,
                "description": "This is a test event",
                "event_type": "test",
                "createdAt": "2020-01-01T00:00:00.000Z",
                "creator": owner_data
            },
            {
                "uuid": self.event2_uuid.bytes,
                "description": "This is a test event",
                "event_type": "test",
                "createdAt": "2020-01-01T00:00:00.000Z",
                "creator": owner_data
            }
        ]

        data_hive = {
            "uuid": None,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Missing data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": None,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Missing data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": None,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Missing data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": None,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Missing data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": None,
            "weight": 37.5,
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Missing data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": None,
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Missing data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": None
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Missing data" in str(context.exception))

    def test_raise_exception_if_data_is_not_valid(self):
        owner_data = {
            "uuid": self.uuid_owner.bytes,
            "name": "John Doe"
        }

        events_data = [
            {
                "uuid": self.event1_uuid.bytes,
                "description": "This is a test event",
                "event_type": "test",
                "createdAt": "2020-01-01T00:00:00.000Z",
                "creator": owner_data
            },
            {
                "uuid": self.event2_uuid.bytes,
                "description": "This is a test event",
                "event_type": "test",
                "createdAt": "2020-01-01T00:00:00.000Z",
                "creator": owner_data
            }
        ]

        data_hive = {
            "uuid": "self.uuid_hive.bytes",
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Invalid data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": "self.uuid_station.bytes",
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Invalid data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": "owner_data",
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Invalid data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": "20.0",
            "sound_level": 67.3,
            "weight": 37.5,
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Invalid data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": "67.3",
            "weight": 37.5,
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Invalid data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": "37.5",
            "events": events_data
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Invalid data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": "events_data"
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Invalid data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": [events_data]
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Invalid data" in str(context.exception))

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": [events_data, events_data]
        }
        with self.assertRaises(Exception) as context:
            Hive(data_hive)
            self.assertTrue("Invalid data" in str(context.exception))

    def test_empty_events(self):
        owner_data = {
            "uuid": self.uuid_owner.bytes,
            "name": "John Doe"
        }

        data_hive = {
            "uuid": self.uuid_hive.bytes,
            "station_uuid": self.uuid_station.bytes,
            "owner": owner_data,
            "temperature": 20.0,
            "sound_level": 67.3,
            "weight": 37.5,
            "events": []
        }
        hive = Hive(data_hive)
        self.assertEqual(hive.last_events, [])

    @classmethod
    def tearDownClass(cls):
        print(Fore.YELLOW + ">>>>>> End of Hive tests" + Fore.RESET)

    @classmethod
    def setUpClass(cls):
        print(Fore.GREEN + ">>>>>> Start of Hive tests" + Fore.RESET)