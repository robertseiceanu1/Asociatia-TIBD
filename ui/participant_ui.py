from service.event_service import EventService
from ui.event_ui import EventUI
from service.participant_service import ParticipantService
from service.statistics_service import StatisticsService
from datetime import date


class ParticipantUI:
    def __init__(self, event_service: EventService, event_ui: EventUI, participant_service: ParticipantService,
                 statistics_service: StatisticsService):
        self.__event_ui = event_ui
        self.__participant_service = participant_service
        self.__event_service = event_service
        self.__statistics_service = statistics_service

    def print_menu(self):
        print("\nParticipant interface\n\n"
              "Options:\n"
              "1.Show all events\n"
              "2.Subscribe to an event\n"
              "3.Show events next week\n"
              "4.Show events by month\n"
              "5.Go to organizer mode\n"
              "6.Add a participant\n"
              "0.Back\n")

    def show_all(self):
        for participant in self.__participant_service.get_all_participants():
            print(participant)

    def participant_mode_run(self):
        while True:
            self.print_menu()
            command = 0
            try:
                command = int(input("Choose the command: ").strip())

            except ValueError:
                print("\nChoose a valid option!\n")

            except KeyboardInterrupt:
                print("\nChoose a valid option!\n")

            if command == 0:
                break
            elif command == 1:
                self.__event_ui.show_all()
            elif command == 2:
                event_id = input("ID of the event you would like to sign up to: ")
                participant_name = input("Enter your name: ")
                self.__participant_service.subscribe_to_an_event(event_id, participant_name)
            elif command == 3:
                self.__show_events_next_week()
            elif command == 4:
                self.__show_events_by_month()
            elif command == 5:
                print("Choose 'Organizer mode' in the options below\n")
                break
            elif command == 6:
                self.__participant_service.add_participant()

    def by_no_of_available_places(self, event):
        return event.get_available_places()

    def __show_events_next_week(self):
        today = date.today()
        self.__event_service.get_all_events().sort(reverse=False, key=self.by_no_of_available_places)
        for event in self.__event_service.get_all_events():
            if (event.get_starting_date() - today).days < 7:
                print(event)

    def by_length(self, event):
        return (event.get_end_date() - event.get_starting_date()).days

    def __show_events_by_month(self):
        self.__event_service.get_all_events().sort(reverse=False, key=self.by_length)
        for i in range(12):
            print(f"Month {i}:")
            for event in self.__event_service.get_all_events():
                if event.get_starting_date().month == i:
                    print(event.get_title())
                    print(' ')
            print()
