# import pymongo
#
# client = pymongo.MongoClient()
# db = client.traveldata
# import requests
# from lxml import html
#
#
# def parse_city():
#     f = open(r'C:\Users\sweet\PycharmProjects\Chatbot3.0\DataBase\urls_to_parse\1', "r", encoding="utf-8")
#     city = f.readlines()
#
#     f.close()
#
#     # print states
#
#
#     city_data = {}
#
#
#     for x in range(0, 10):
#         city_url = city[x]
#         lst = city_url.split('/')
#         city_name = lst[4]
#         print(city_name)
#         if db.rajdata.find({"name":city_name}).count() == 0 :
#             city_url1 = city_url.strip()
#             city_data['name'] = city_name.lower()
#             city_data['type'] = 'city'
#             print(city_name)
#             response = requests.get(city_url1)
#             tree = html.fromstring(response.text)
#
#             # for city rating
#             city_rating = tree.xpath(".//span[@class='int-banner-rating-num']/text()")[0]
#             city_data['ratings'] = city_rating
#
#             # Famous for
#             # city_famous = tree.xpath("//div[@class='button-category dest-sprite destination-detail-heritage']//text()")
#             # print city_famous
#             # city_data['Famous_for'] = city_famous.lower()
#
#             # Travel Guide
#             city_guide = 'http://www.holidayiq.com/travel-guides/' + city_name + '.pdf'
#             city_data['travel_guide'] = city_guide
#
#             # rank
#             # temp1 = tree.xpath('//div[@class="rank-bar"]//span//text()')
#             # temp2 = temp1.split()
#             # city_rank = temp2[0] + ' ' + temp2[1] + ' ' + temp2[2] + ' ' + temp2[3]
#             # city_data['city_rank'] = city_rank
#
#             # State name
#             city_statename = 'rajhasthan'
#             city_data['city_statename'] = city_statename
#
#             # Best Time
#             city_bestTime = ['November', 'December', 'February', 'March']
#             city_data['city_bestTime'] = city_bestTime
#
#             # user reviews
#             city_reviews = tree.xpath("//div[@id='review-rating-tab']/div/div[2]/div//text()")[7]
#             city_data['city_reviews'] = city_reviews
#
#             # Things to do in city(pending)
#             # l=tree.xpath('//div[@id="longDescription11"]//p//text()')
#             # print state_data
#             # Inserting one city's data as a dictionary record in DB
#             city_details = tree.xpath("/html/body/div[1]/div/div[5]/div/div/div[1]/div/div[20]/div/div//text()")
#             city_data['city_details'] = city_details
#
#             city_famous_for = tree.xpath("//h3[@class='attr-caption-head itinerary-attr-caption-head']//text()")
#             city_data['city_famous_for'] = city_famous_for
#
#             city_photos = tree.xpath("//img[@class='attr-img-height slick-slide-img']/@src")
#
#
#             city_data['city_images'] = city_photos[0]
#
#
#
#             db.rajdata.insert(city_data.copy())
#
#
#
# if __name__ == "__main__":
#     parse_city()
