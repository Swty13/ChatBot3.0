import pymongo
client = pymongo.MongoClient()
db = client.traveldata
import requests
from lxml import html

client = pymongo.MongoClient()
db = client.traveldata



def parse_reach():
    f = open(r'C:\Users\sweet\PycharmProjects\Chatbot3.0\DataBase\urls_to_parse\1', "r", encoding="utf-8")
    city = f.readlines()

    f.close()

    # print states

    city_data = {}
    for x in range(0, 10):
        city_url = city[x]
        lst = city_url.split('/')
        city_name = lst[4].split('-')[0]

        city_url1 = city_url.strip()
        print(city_name)
        if db.reach.find({"city_name":city_name}).count() == 0 :

                mode_dict = {}
                response = requests.get(city_url1)
                tree = html.fromstring(response.text)

                link_reach = tree.xpath("/html/body/div[1]/div/div[5]/div/div/div[1]/div/div[1]/div/div/div[7]/div/a/@href")[0]
                print(link_reach)

                response_reach = requests.get(link_reach)
                tree_reach = html.fromstring(response_reach.text)


                # for train
                mode_list = ['By Bus','By Train','By Flight','By Cab/Taxi']
                city_data['city_name'] = city_name
                k = 0
                for i in range(2, 6):
                    try:
                        desc = ''

                        mode = tree_reach.xpath("/html/body/div[2]/div[1]/div[6]/div[2]/div[1]/div[1]/div[4]/div/p[" + str(i) + "]//text()")
                        try:
                            for x in range(1, len(mode)):
                                desc = desc + mode[x].strip()
                            print(desc)
                            if desc == '':
                                desc = "Sorry, but this information is not available!!"
                        except:
                            desc = "Sorry, but this information is not available!!"
                        city_data[mode_list[k]] = desc
                        k = k + 1
                    except:
                        desc = "Sorry, but this information is not available!!"
                        city_data[mode_list[k]] = desc
                        k = k + 1
                    # INSERTING one city reach data as a dictionary record in DB
                print(city_data)

                db.reach.insert(city_data.copy())


if __name__ == "__main__":
	parse_reach()


