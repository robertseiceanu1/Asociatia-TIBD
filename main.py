from ui.event_ui import EventUI
from ui.participant_ui import ParticipantUI
from service.event_service import EventService
from service.participant_service import ParticipantService
from service.statistics_service import StatisticsService
from ui.starting_ui import StartingUI


event_service = EventService('data')
participant_service = ParticipantService('data')

event_service.set_participant_service(participant_service)
participant_service.set_event_service(event_service)

statistics_service = StatisticsService(event_service, participant_service)

event_ui = EventUI(event_service, participant_service, statistics_service)
participant_ui = ParticipantUI(event_service, event_ui, participant_service, statistics_service)

ui = StartingUI(event_ui, participant_ui)
ui.starting_mode_run()
