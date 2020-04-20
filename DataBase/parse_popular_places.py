# import pymongo
# import requests
# from lxml import html
#
# client = pymongo.MongoClient()
# db = client.popularplaces_rajasthan
#
# places=["Jaisalmer","Jaipur","Jodhpur","Bundi","Bikaner","Ajmer","Pushkar","Udaipur","Mount Abu","Sawai Madhopur","Bharatpur","Alwar          ","Pali           ","Chittorgarh    ",
# "Hanumangarh","Jhunjhunu","Jhalawar","Churu","Kota","Sikar","Rajasthan"]
# def parse_popularplaces_rajasthan():
#                 f = open(r'C:\Users\sweet\PycharmProjects\Chatbot3.0\DataBase\popular_places_rajasthan.txt', "r", encoding="utf-8")
#                 city = f.readlines()
#
#                 f.close()
#
#                 city_data = {}
#                 for x in range(0, 8):
#                     city_url = city[x]
#
#                     mode_dict = {}
#                     response = requests.get(city_url)
#                     print(city_url)
#                     tree = html.fromstring(response.text)
#
#                     description = tree.xpath("/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/p/text()[1]")
#                     print(description)
#
#                     # response_reach = requests.get(link_reach)
#                     # tree_reach = html.fromstring(response_reach.text)
#                     #
#                     #
#                     # # for train
#                     # mode_list = ['By Bus','By Train','By Flight','By Cab/Taxi']
#                     # city_data['city_name'] = city_name
#                     # k = 0
#                     # for i in range(2, 6):
#                     #     try:
#                     #         desc = ''
#                     #
#                     #         mode = tree_reach.xpath("/html/body/div[2]/div[1]/div[6]/div[2]/div[1]/div[1]/div[4]/div/p[" + str(i) + "]//text()")
#                     #         try:
#                     #             for x in range(1, len(mode)):
#                     #                 desc = desc + mode[x].strip()
#                     #             print(desc)
#                     #             if desc == '':
#                     #                 desc = "Sorry, but this information is not available!!"
#                     #         except:
#                     #             desc = "Sorry, but this information is not available!!"
#                     #         city_data[mode_list[k]] = desc
#                     #         k = k + 1
#                     #     except:
#                     #         desc = "Sorry, but this information is not available!!"
#                     #         city_data[mode_list[k]] = desc
#                     #         k = k + 1
#                     #     # INSERTING one city reach data as a dictionary record in DB
#                     # print(city_data)
#                     #
#                     # # db.reach.insert(city_data.copy())
#
#
# if __name__ == "__main__":
# 	parse_popularplaces_rajasthan()
#
#
