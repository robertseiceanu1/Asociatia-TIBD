class Participant:
    def __init__(self, name: str, photo_link: str, subscribed_events: list):
        self.__name = name
        self.__photo_link = photo_link
        self.__subscribed_events = subscribed_events

    def get_name(self):
        return self.__name

    def get_photo_link(self):
        return self.__photo_link

    def get_subscribed_events(self):
        return self.__subscribed_events

    def set_name(self, new_name):
        self.__name = new_name

    def set_photo_link(self, new_photo_link):
        self.__photo_link = new_photo_link

    def set_subscribed_events(self, new_subscribed_events):
        self.__subscribed_events = new_subscribed_events

    def __str__(self):
        return f"Name: {self.__name} \n" \
               f"Photo link: {self.__photo_link} \n" \
               f"Subscribed events: {self.__subscribed_events}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_name() == other.get_name()
