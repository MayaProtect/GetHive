from uuid import UUID
from app.owner import Owner
from app.event import Event
from bson.binary import Binary


class Hive:
    def __init__(self, hive):
        if hive['uuid'] is None:
            raise ValueError("The hive must have an uuid")

        if type(hive['uuid']) is not bytes and type(hive['uuid']) is not Binary:
            raise TypeError("The hive uuid must be a UUID, not a " + str(type(hive['uuid'])))

        if hive['owner'] is None:
            raise ValueError("The hive must have an owner")

        if hive['station_uuid'] is None:
            raise ValueError("The hive must have an station_uuid")

        if type(hive['station_uuid']) is not bytes and type(hive['station_uuid']) is not Binary:
            raise TypeError("The hive station_uuid must be a UUID, not a " + str(type(hive['station_uuid'])))

        self.id = UUID(bytes=hive['uuid'])
        self.owner = Owner(hive['owner'])
        self.station = UUID(bytes=hive['station_uuid'])
        self.last_temperature = hive['temperature'] if hive['temperature'] is not None else 0.0
        self.last_weight = hive['weight'] if hive['weight'] is not None else 0.0
        self.last_sound_level = hive['sound_level'] if hive['sound_level'] is not None else 0.0
        self.last_events = []
        try:
            for event in hive['events']:
                self.__addEvent(Event(event))
        except Exception as e:
            raise e

    def __addEvent(self, event):
        """
        Add an event to the hive
        :param event:
        :return:
        """
        self.last_events.append(event)
        self.last_events.sort(key=lambda x: x.createdAt, reverse=True)
        self.last_events = self.last_events[:10]

    def __event_to_json(self):
        """
        Convert the last events to json
        :return:
        """
        events = []
        for event in self.last_events:
            events.append(event.__to_json__())
        return events

    def __to_json__(self):
        """
        Convert the hive to json
        :return:
        """
        return {
            "id": str(self.id),
            "owner": self.owner.__to_json__(),
            "station": str(self.station),
            "last_temperature": self.last_temperature,
            "last_sound_level": self.last_sound_level,
            "last_weight": self.last_weight,
            "last_events": self.__event_to_json()
        }