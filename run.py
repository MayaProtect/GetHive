from app import GetHive
from os import environ as env


def main():
    params = {
        "mongo_host": env.get("MONGO_HOST", "localhost"),
        "mongo_port": env.get("MONGO_PORT", "27017"),
        "mongo_db": env.get("MONGO_DB", "mayaprotect")
    }
    hive = GetHive(params)
    hive.run()


if __name__ == '__main__':
    main()
    