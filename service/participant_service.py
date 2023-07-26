from domain.participant import Participant
from repository.repository import Repository
import pickle
from os.path import exists


class ParticipantService:
    def __init__(self, data_folder, event_service):
        self.__data_folder = data_folder
        self.participants_file = f"{data_folder}/participants_file"
        saved_participants = self.__load()
        self.__repository = Repository(saved_participants)
        self.__event_service = event_service

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

    def participant_exists(self, name):
        return self.__repository.find_position(Participant(name, "", [])) is not None

    def get_all_participants(self):
        return self.__repository.get_all()

    def get_participant(self, participant_name):
        return self.__repository.find(Participant(participant_name, "", []))

    def subscribe_to_an_event(self, event_id):

        event_to_subscribe = self.__event_service.get_event(event_id)

        if event_to_subscribe.get_available_places() - event_to_subscribe.get_no_of_participants() > 0:
            participant_name = input("Name: ")
            if self.participant_exists(participant_name):
                participant = self.get_participant(participant_name)
                subscribed_events = participant.get_subscribed_events()
                if event_id in subscribed_events:
                    print("Already subscribed!")
                else:
                    subscribed_events.append(event_id)
            else:
                participant = Participant(participant_name, "", [event_id])
                participant.set_photo_link(input("Photo link: "))
                self.__repository.add(participant)
            self.__save()

            # modifying the number of participants in the event
            event_to_subscribe.set_no_of_participants(event_to_subscribe.get_no_of_participants() + 1)
            self.__event_service.save()
        else:
            raise Exception("No places left!")
