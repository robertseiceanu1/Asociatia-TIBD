from datetime import date
from domain.participant import Participant
from domain.event import Event
from repository.repository import Repository
import pickle
from os.path import exists


class ParticipantService:
    def __init__(self, data_folder):
        self.__data_folder = data_folder
        self.participants_file = f"{data_folder}\participants_file"
        saved_participants = self.__load()
        self.__repository = Repository(saved_participants)

    def __load(self):
        if exists(self.participants_file):
            file = open(self.participants_file, 'rb')
            participants = pickle.load(file)
            file.close()
            return participants
        else:
            return []

    def __save(self):
        file = open(self.participants_file, 'wb')
        pickle.dump(self.get_all_participants(), file)
        file.close()

    def add_participant(self):
        new_participant = Participant("", "", [])
        print("Give information about participant: \n")

        new_participant.set_name(input("Name: "))
        new_participant.set_photo_link(input("Photo link: "))

        events_input = input("Subscribed events: ")
        new_participant.set_subscribed_events(events_input.split())
        self.__repository.add(new_participant)
        self.__save()

    def participant_exists(self, name):
        return self.__repository.find_position(Participant(name, "", [])) is not None

    def get_all_participants(self):
        return self.__repository.get_all()

    def get_participant(self, participant_name):
        return self.__repository.find(Participant(participant_name, "", []))

    def subscribe_to_an_event(self, event_id, participant_name):

        event_to_subscribe = self.__repository.find(
            Event(event_id, "", "", 0, 0, date(2023, 1, 1), date(2023, 1, 1), ""))

        if event_to_subscribe.get_available_places() - event_to_subscribe.get_no_of_participants() > 0:

            # modifying the number of participants in the event
            event_to_subscribe.set_no_of_participants(event_to_subscribe.get_no_of_participants() + 1)
            event_to_subscribe_title = event_to_subscribe.get_title()
            participant_to_subscribe = self.get_participant(participant_name)

            # modifying the participant's subscribed events
            participant_subscribed_events = participant_to_subscribe.get_subscribed_events()
            participant_subscribed_events.append(event_to_subscribe_title)
            self.__save()
        else:
            raise Exception("No places left!")
