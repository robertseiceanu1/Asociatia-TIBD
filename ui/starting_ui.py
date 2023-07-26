from ui.event_ui import EventUI
from ui.participant_ui import ParticipantUI


class StartingUI:
    def __init__(self, event_ui: EventUI, participant_ui: ParticipantUI):
        self.__event_ui = event_ui
        self.__participant_ui = participant_ui

    def __print_menu(self):
        print("Starting interface\n\n"
              "Options:\n"
              "1.Organizer mode\n"
              "2.Participant mode\n"
              "0.Exit\n")

    def starting_mode_run(self):
        while True:
            self.__print_menu()
            command = -1
            try:
                command = int(input("Choose the command: ").strip())
            except ValueError:
                print("\nChoose a valid option!\n")

            if command == 0:
                break
            elif command == 1:
                self.__event_ui.organizer_mode_run()
            elif command == 2:
                self.__participant_ui.participant_mode_run()
