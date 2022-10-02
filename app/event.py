from app.owner import Owner
from bson.binary import Binary
from uuid import UUID


class Event:
    def __init__(self, event):
        event = event[0]
        if event['uuid'] is None:
            raise ValueError("The event must have an uuid")

        if type(event['uuid']) is not bytes and type(event['uuid']) is not Binary:
            raise TypeError("The event uuid must be a UUID")

        if event['eventType'] is None:
            raise ValueError("The event must have an event_type")

        if type(event['eventType']) is not str:
            raise TypeError("The event event_type must be a string")

        if event['createdAt'] is None:
            raise ValueError("The event must have a created_at")

        if type(event['createdAt']) is not str:
            raise TypeError("The event created_at must be a string")

        if event['owner'] is None:
            raise ValueError("The event must have a creator")

        if event['description'] is None:
            raise ValueError("The event must have a description")

        self.id = UUID(bytes=event['uuid'])
        self.description = event['description']
        self.event_type = event['eventType']
        self.createdAt = event['createdAt']
        self.creator = Owner(event['owner'])

    def __to_json__(self):
        """
        Convert the event to json
        :return:
        """
        return {
            "id": str(self.id),
            "description": self.description,
            "event_type": self.event_type,
            "createdAt": self.createdAt,
            "creator": self.creator.__to_json__()
        }