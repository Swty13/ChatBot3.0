import pymongo
client = pymongo.MongoClient()
db = client.traveldata
import requests
from lxml import html

def parse_state():

    f = open(r'C:\Users\sweet\PycharmProjects\Chatbot3.0\DataBase\urls_to_parse\0', "r",encoding="utf-8")
    states = f.readlines()
    f.close()

    # print states
    states_DS = []
    state_data = {}
    # only storing user-reviews, for sentiment analysis
    states_DS2 = []
    state_data2 = {}

    for x in range(0, 4):
        state_url = states[x]
        lst = state_url.split('/')
        st_name = lst[4]

        state_data['name'] = st_name.lower()
        state_data['type'] = 'state'
        state_data2['name'] = st_name.lower()
        response = requests.get(state_url)
        tree = html.fromstring(response.text)

        # for state rating
        # st_rating = tree.xpath("//div[starts-with(@class,'rating-container')]/@title")[0]
        st_rating = tree.xpath("//div[starts-with(@class,'rating-container')]/@title")
        state_data['ratings'] = st_rating

        # for description
        l = []
        l = tree.xpath('//div[@id="longDescriptionOne"]//span//p//span//text()')
        st_desc = ""
        for item in l:
            try:
                st_desc = str(st_desc + str(item))
                print (str(item))
            except:
                continue
        state_data['details'] = st_desc

        # for vedio rating
        # video = tree.xpath("//div[@class='footer-bottom-icon']//a/@href")[3]
        video = tree.xpath("//div[@class='footer-bottom-icon']//a/@href")
        state_data['video_review'] = video

        # for list of cities/destinations
        l = tree.xpath("//div[@class='about-photo']//h5//a//text()")
        temp = []
        for place in l:
            l2 = place.split(',')
            temp.append(l2[0].lower())
    state_data['places'] = temp

    # for list of cities/destinations ---- user reviews
    l = tree.xpath("//div[@class='review-block ']//blockquote//text()")
    state_data['reviews'] = l
    state_data2['reviews'] = l

    # print state_data
    # INSERTING one state's data as a dictionary record in DB
    db.destinations.insert(state_data.copy())
    states_DS.append(state_data)
    states_DS2.append(state_data2)




