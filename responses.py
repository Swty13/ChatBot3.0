import pymongo
import Preprocessing.spell as sp
import random
from Preprocessing.named_entity import entity_recog

client = pymongo.MongoClient()
db = client.traveldata


class Response_Functions:
    def __init__(self):
        self.data = []

    def get_description(self, ids):
        try:
            record = db.rajdata.find({"name": ids.lower()})[0]
            print(record)
        except:
            return "No description available for this place."

        if record["type"] == 'state':
            return record['city_images'] + '*' + record['city_details']

        elif record["type"] == 'city':
            if ids == "jaisalmer":
                strn = record['city_images'] + '*' + record['city_details']
                return strn
            strn = record['city_images'] + '*' + record['city_details'][2]
            return strn
        elif record["type"] == 'place':
            strn = record['place_images'] + '*' + record['place_details']
            return strn
        else:
            return "Sorry we could not get you. Can you be more specific."

    def get_nearby_places(self, ids):
        try:

            record = db.rajdata.find({"name": ids.lower()})[0]

        except:
            return "Please provide a place in Rajasthan to know its details!!"

        try:
            res_list = ["According to Traveller feedback,There are many places like:", "Suggested by Travellers,\n",
                        "Several Travellers have given,\n", "Travellers say,\n"]

            strn = res_list[0]
            for i in range(0, 5):
                strn = strn + record['city_famous_for'][i] + ","
            print(strn)

        except:
            strn = "Sorry we could not get you. Can you be more specific."
        return strn

    def get_rating(self, ids):

        try:
            record = db.rajdata.find({"name": ids.lower()})[0]
            print(record)
        except:
            return "Please provide a place in Rajasthan to know its Rating!!"
        counter = (random.randint(0, 3))
        res_list = ["According to Traveller feedback,\n", "Suggested by Travellers,\n",
                    "Several Travellers have given,\n", "Travellers say,\n"]
        try:
            strn = res_list[counter] + record["ratings"]

        except:
            strn = "Sorry we could not get you. Can you be more specific."
        return strn

    def get_review(self, ids):
        try:
            record = db.rajdata.find({"name": ids.lower()})[0]

        except:
            return "Please provide a place in Rajasthan to know its Review!!"
        try:
            strn = "Dear Traveller " + ids.title() + " Reviews are as follows,\n"
            strn = strn + ">> " + str(record['city_reviews'])
        except:
            strn = "Sorry we could not get you. Can you be more specific."
        return strn

    def get_plan(self, ids):
        try:
            record = db.rajdata.find({"name": ids[0].lower()})[0]
        except:
            return "We are so Sorry! No plan itinerary available for this place."

        strn = record["travel_guide"]
        return strn

    def get_how_to_reach(self, ids):

        try:
            record = db.reach.find({"city_name": ids[0].lower()})[0]
            print(record)
        except:
            return "Sorry we could not get you. Can you be more specific."
        if len(ids) > 1:
            if ids[1] == 'bus':
                strn = record['By Bus']
            elif ids[1] == 'train' :
                strn = record['By Train']
            elif ids[1] == 'flight' or ids[1] == 'plane':
                strn = record['By Flight']
            elif ids[1] == 'cab' or ids[1] == 'cab' == 'taxi':
                strn = record['By Cab/Taxi']
            else:
                strn = record['By Bus']
            return strn
        else:
            strn = record['By Bus']
            return strn

    def best_time(self, ids):
        records = []
        try:
            record = db.rajdata.find({'name': ids.lower()})
            for i in record:
                records.append(i)

        except:
            return "Sorry we could not get you. Can you be more specific."

        if records[0]["type"] == "city":
            strn = "Best time to visit " + ids + " is " + " ".join(records[0]["city_bestTime"])
        else:
            strn = "Please specify city name!"

        return strn

    def get_greeting(self, tag):
        try:
            if tag == "greeting":
                greeting_response = [ "How are you ?? I'm Sana",
                                      "How can i help you??", "How may i assit you??"]

                return random.choice(greeting_response)
            elif tag == "goodbye":
                goodbye_response = ['Sad to see you go', 'Talk to you later', 'Goodbye']
                return random.choice(goodbye_response)
        except:
            return "Can you say that again?."


def query_handling(input, tag):
    obj = Response_Functions()
    missed_response = ["Can you say that again?", "I missed what you said. Say it again?",
                       "Sorry, I didn't get that.", "Sorry, what was that"]
    if tag == 'greeting' or tag == 'goodbye':
        return obj.get_greeting(tag)


    if tag == 'miscellaneous':
        response = ["... 🤔 Bhakkk...I don't understand your question. " ]
        return random.choice(response)

    if tag == 'assist':
        response = ["How can I help you today?😁",
                    "Sure, what can I help you with?😄😄",
                    "Let me know what you need, I'd be glad to help.😃",
                    "Tell me how can I help you?😁😁"]
        return random.choice(response)

    if tag == 'bot':
        response = ["Hi I am Sana your travel chatbot to Rajasthan 😉😉",
                    "I am Sana your travel virtual assistant😊😊",
                    "Welcome to Rajasthan travel chatbot,I am Sana Glad to meet you😉😉"
                    ]
        return random.choice(response)

    if tag == 'info':
        response = ["For more Information you can visit this site:https://www.holidayiq.com/"]
        return random.choice(response)

    response = entity_recog(input)
    if not response:
        return random.choice(missed_response)



    if tag == 'place':
        return obj.get_description(response[0])

    elif tag == 'nearby places':

        return obj.get_nearby_places(response[0])





    elif tag == 'besttime':

        return obj.best_time(response[0])


    elif tag == 'review':

        return obj.get_review(response[0])


    elif tag == 'rating':

        return obj.get_rating(response[0])


    elif tag == 'reach':
        return obj.get_how_to_reach(response)


    elif tag == 'plan':
        return obj.get_plan(response)


    else:
        return random.choice(missed_response)
