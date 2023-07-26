from service.event_service import EventService
from service.participant_service import ParticipantService
from service.statistics_service import StatisticsService


class EventUI:
    def __init__(self, event_service: EventService, participant_service: ParticipantService,
                 statistics_service: StatisticsService):
        self.__event_service = event_service
        self.__participant_service = participant_service
        self.__statistics_service = statistics_service

    def __print_menu(self):
        print("\nOrganizer interface\n\n"
              "Options:\n"
              "1.Add event\n"
              "2.Delete event\n"
              "3.Edit event\n"
              "4.Show all events\n"
              "5.Show all city events\n"
              "6.Show all event participants\n"
              "7.Show all events with participants\n"
              "0.Back\n")

    def show_all(self):
        all_events = self.__event_service.get_all_events()
        if len(all_events) == 0:
            print("No events!")
        else:
            for event in all_events:
                print(event)

    def organizer_mode_run(self):
        while True:
            self.__print_menu()
            command = -1
            try:
                command = int(input("Choose the command: ").strip())
            except ValueError:
                print("\nChoose a valid option!")

            if command == 0:
                break
            elif command == 1:
                print("Give information about event: \n")
                self.__event_service.add_event()
            elif command == 2:
                self.__event_service.delete_event()
            elif command == 3:
                event_id = input("ID of event you want to modify: ")
                print("What would you like to change? Press ENTER if you don't want to modify the field\n")
                self.__event_service.edit_event(event_id)
            elif command == 4:
                self.show_all()
            elif command == 5:
                city = input("City you want to see the events of: ")
                self.__show_all_city_events(city)
            elif command == 6:
                event_id = int(input("ID of event you want to see the participants of: "))
                self.__show_all_event_participants(event_id)
            elif command == 7:
                self.show_all_events_with_participants()

    def __show_all_city_events(self, city):
        any_event = 0
        for event in self.__event_service.get_all_events():
            if event.get_city() == city:
                print(f"[{event.get_event_id()}] {event.get_title()} - {event.get_city()}")
                any_event = 1
        if any_event == 0:
            print("No events!")

    def __show_all_event_participants(self, event_id):
        any_participant = 0
        for participant in self.__participant_service.get_all_participants():
            for e_id in participant.get_subscribed_events():
                if e_id == event_id:
                    print(participant)
                    any_participant = 1
        if any_participant == 0:
            print("No participants!")

    def by_no_of_participants(self, event):
        return event.get_no_of_participants()

    def show_all_events_with_participants(self):
        self.__event_service.get_all_events().sort(reverse=True, key=self.by_no_of_participants)
        any_event = 0
        for event in self.__event_service.get_all_events():
            if int(event.get_no_of_participants()) > 0:
                print(event)
                any_event = 1
        if any_event == 0:
            print("No events!")
