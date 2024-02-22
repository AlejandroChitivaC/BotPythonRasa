# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
import locale


class ActionGetCurrentDate(Action):
    def name(self) -> Text:
        return "action_get_current_date"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        locale.setlocale(locale.LC_TIME, 'Es_ES')
        current_date = datetime.now().strftime("%B %d %Y")
        dispatcher.utter_message(template="utter_current_date", text=current_date)

        return [SlotSet("date", current_date)]
