from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    ActionExecuted,
    UserUtteranceReverted,
    SlotSet
)


class RepeatedIntent(Action):

    def name(self) -> Text:
        return "action_count_repeated_intent"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        user_events = [event for event in reversed(tracker.events) if event['event'] == "user"]

        user_intents = [event.get("parse_data", {}).get("intent", {}).get("name") for event in user_events]

        current_intent = user_intents.pop(0)

        repeated_intent_count = 0
        for intent in user_intents:
            if intent != current_intent:
                break
            repeated_intent_count += 1

        return [SlotSet("repeated_intent_counter", repeated_intent_count)]
