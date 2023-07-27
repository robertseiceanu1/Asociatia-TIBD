from service.event_service import EventService
from service.participant_service import ParticipantService


class StatisticsService:
    def __init__(self, event_service: EventService, participant_service: ParticipantService):
        self.__event_service = event_service
        self.__participant_service = participant_service
        pass

    def show_stats(self):
        print(f"Events: {len(self.__event_service.get_all_events())}")
        print(f"Participants: {len(self.__participant_service.get_all_participants())}")
