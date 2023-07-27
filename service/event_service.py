from domain.event import Event
from repository.repository import Repository
from datetime import date
from os.path import exists
import pickle
import qrcode

from service.participant_service import ParticipantService


class EventService:
    def __init__(self, data_folder):
        self.__participant_service = None
        self.__data_folder = data_folder
        self.events_file = f"{data_folder}/events_file"
        saved_events = self.__load()
        self.__repository = Repository(saved_events)

    def __qr_code(self, website, event_id):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=10,
        )
        qr.add_data(website)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{self.__data_folder}/event_{event_id}.png")

    def __load(self):
        if exists(self.events_file):
            file = open(self.events_file, 'rb')
            events = pickle.load(file)
            file.close()
            return events
        else:
            return []

    def set_participant_service(self, participant_service: ParticipantService):
        self.__participant_service = participant_service

    def save(self):
        file = open(self.events_file, 'wb')
        pickle.dump(self.get_all_events(), file)
        file.close()

    def add_event_input(self):
        new_event = Event("0", "", "", 0, 0, date(2023, 1, 1), date(2023, 1, 1), "")
        new_event.set_event_id(input("ID: "))
        new_event.set_title(input("Title: "))
        new_event.set_city(input("City: "))
        new_event.set_no_of_participants(0)
        new_event.set_available_places(int(input("Available places: ")))
        new_event.set_starting_date(date.fromisoformat(input("Starting date (YYYY-MM-DD): ")))
        new_event.set_end_date(date.fromisoformat(input("End time (YYYY-MM-DD): ")))
        new_event.set_website(input("Website: "))
        self.add_event(new_event)

    def add_event(self, event: Event):
        self.__repository.add(event)
        self.__qr_code(event.get_website(), event.get_event_id())
        self.save()
        print(f"Event added: {event.get_title()}")

    def event_exists(self, event_id):
        return self.__repository.find_position(
            Event(event_id, "", "", 0, 0, date(2023, 1, 1), date(2023, 1, 1), "")) is not None

    def delete_event(self):
        event_id = input("Event id: ").strip()
        event = Event(event_id, "", "", 0, 0, date(2023, 1, 1), date(2023, 1, 1), "")
        if self.event_exists(event_id):
            self.__repository.delete(event)
            self.__participant_service.unsubscribe_all(event_id)
            self.save()
        else:
            raise Exception(f"Event with ID {event_id} does not exist!")

    def get_all_events(self):
        return self.__repository.get_all()

    def get_event(self, event_id):
        return self.__repository.find(Event(event_id, "", "", 0, 0, date(2023, 1, 1), date(2023, 1, 1), ""))

    def edit_event(self, event_id):
        if self.event_exists(event_id):
            edited_event = self.__repository.find(Event(event_id, "", "", 0, 0, date(2023, 1, 1), date(2023, 1, 1), ""))
            new_title = input("Title: ")
            if new_title != '':
                edited_event.set_title(new_title)

            new_city = input("City: ")
            if new_city != '':
                edited_event.set_city(new_city)

            new_available_places = input("Available places: ")
            if new_available_places != '':
                edited_event.set_available_places(new_available_places)

            new_starting_time = input("Starting time: ")
            if new_starting_time != '':
                edited_event.set_starting_date(date.fromisoformat(new_starting_time))

            new_end_time = input("End time: ")
            if new_end_time != '':
                edited_event.set_end_date(date.fromisoformat(new_end_time))

            new_website = input("Website: ")
            if new_website != '':
                edited_event.set_website(new_website)
                self.__qr_code(new_website, event_id)
            self.save()
