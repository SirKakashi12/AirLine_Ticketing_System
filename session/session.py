class Session:
    data = {}

    @staticmethod
    def set(key, value):
        Session.data[key] = value

    @staticmethod
    def get(key):
        return Session.data.get(key, None)

    @staticmethod
    def exists(key):
        return key in Session.data

    @staticmethod
    def clear():
        Session.data.clear()
