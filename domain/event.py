from datetime import date


class Event:
    def __init__(self, event_id: str, title: str, city: str, no_of_participants: int, available_places: int,
                 starting_date: date, end_date: date, website: str):
        self.__event_id = event_id
        self.__title = title
        self.__city = city
        self.__no_of_participants = no_of_participants
        self.__available_places = available_places
        self.__starting_date = starting_date
        self.__end_date = end_date
        self.__website = website

    def get_event_id(self):
        return self.__event_id

    def get_title(self):
        return self.__title

    def get_city(self):
        return self.__city

    def get_no_of_participants(self):
        return self.__no_of_participants

    def get_available_places(self):
        return self.__available_places

    def get_starting_date(self):
        return self.__starting_date

    def get_end_date(self):
        return self.__end_date

    def get_website(self):
        return self.__website

    def set_event_id(self, new_id):
        self.__event_id = new_id

    def set_title(self, new_title):
        self.__title = new_title

    def set_city(self, new_city):
        self.__city = new_city

    def set_no_of_participants(self, new_no_of_participants):
        self.__no_of_participants = new_no_of_participants

    def set_available_places(self, new_available_places):
        self.__available_places = new_available_places

    def set_starting_date(self, new_starting_time):
        self.__starting_date = new_starting_time

    def set_end_date(self, new_end_time):
        self.__end_date = new_end_time

    def set_website(self, new_website):
        self.__website = new_website

    def __str__(self):
        return f"ID: {self.__event_id} \n" \
               f"Title: {self.__title} \n" \
               f"City: {self.__city} \n" \
               f"Number of participants: {self.__no_of_participants}\n" \
               f"Available places: {self.__available_places} \n" \
               f"Starting time: {self.__starting_date}\n" \
               f"Starting time: {self.__end_date}\n" \
               f"Website: {self.__website}\n"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_event_id() == other.get_event_id()
