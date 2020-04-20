import pymongo
from . import parse_city
from . import parse_state
from . import parse_reach

# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client.traveldata
# print("database ctrated succesfully")
# try:
# 	db.destinations.drop()
# except:
# 	pass




if __name__ == "__main__":
	parse_city()
	parse_state()
	parse_reach()
