from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Calling the DB
        # Calling an API
        # do anything
        # all calculations are done here
        camera = tracker.get_slot('camera')
        ram = tracker.get_slot('RAM')
        battery = tracker.get_slot('battery')
        budget = tracker.get_slot('budget')
        info = tracker.get_slot('info')
        email = tracker.get_slot('email')
        contact = tracker.get_slot('contact')



        dispatcher.utter_message(text='Here are your search results')
        dispatcher.utter_message(text='The features you entered: '+str(camera)+","+str(ram)+","+str(battery)+","+str(budget)+","+str(info)+","+str(email)+","+str(contact))
        return []

class ActionShowLatestNews(Action):

    def name(self) -> Text:
        return "action_show_latest_news"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Calling the DB
        # Calling an API
        # do anything
        # all calculations are done here
        dispatcher.utter_message(text="Here is the latest news for your category")
        return []

class ProductSearchForm(FormAction):

    def name(self) -> Text:

        return "product_search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return ["ram","battery","camera","budget","info","email","contact"]


    def validate_ram(self,value: Text,dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any],) -> Dict[Text, Any]:
        ram_int = int(re.findall(r'[0-9]+',value)[0])
        if ram_int < 16:
            return {"ram":ram_int}
        else:
            dispatcher.utter_message(template="utter_wrong_ram")
            return {"ram":None}

    def validate_camera(self,value: Text,dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any],) -> Dict[Text, Any]:
        camera_int = int(re.findall(r'[0-9]+',value)[0])
        if camera_int < 150:
            return {"camera":camera_int}
        else:
            dispatcher.utter_message(template="utter_wrong_camera")
            return {"camera":None}

    def validate_budget(self,value: Text,dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any],) -> Dict[Text, Any]:
        budget_int = int(re.findall(r'[0-9]+',value)[0])
        if budget_int < 4000:
            return {"budget":budget_int}
        else:
            dispatcher.utter_message(template="utter_wrong_budget")
            return {"budget":None}

    def validate_battery(self,value: Text,dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        battery_int = int(re.findall(r'[0-9]+',value)[0])
        if battery_int < 10000:
            return {"battery":battery_int}
        else:
            dispatcher.utter_message(template="utter_wrong_battery")
            return {"battery":None}

    def validate_contact(self,value: Text,dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        contact_int = int(re.findall(r'[0-9]+',value)[0])
        if len(contact_int) == 10:
            return {"contact":contact_int}
        else:
            dispatcher.utter_message(template="utter_wrong_contact")
            return {"contact":None}



    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Please find your searched items here.....")
        return []
