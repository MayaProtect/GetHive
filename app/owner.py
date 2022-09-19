from uuid import UUID
from bson.binary import Binary


class Owner:
    def __init__(self, owner):
        if owner['uuid'] is None:
            raise ValueError("The owner must have an uuid")

        if type(owner['uuid']) is not bytes and type(owner['uuid']) is not Binary:
            raise TypeError("The owner uuid must be a UUID")

        if 'name' not in owner:
            if owner['firstname'] is None or owner['lastname'] is None:
                raise ValueError("The owner must have a name or a firstname and a lastname")
            else:
                self.name = owner['firstname'] + " " + owner['lastname']
        else:
            self.name = owner['name']

        if type(self.name) is not str:
            raise TypeError("The owner name must be a string")

        self.id = UUID(bytes=owner['uuid'])

    def __to_json__(self):
        """
        Convert the owner to json
        :return:
        """
        return {
            "id": str(self.id),
            "name": self.name
        }
