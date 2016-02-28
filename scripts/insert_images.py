from pymongo import MongoClient
from bson import Binary, Code
import os,json,sys
from bson.json_util import dumps
client = MongoClient()
db = client.robynwlp
table = db.gallery

from datetime import datetime

def buildJSONAndInsert( image_list, source_folder, collection, photographer, website, page ):
	input_json = [{
                "images": imagesFromDirJSON( image_list, source_folder, collection),
                "collection": collection,
                "photographer": photographer,
                "website": website,
		"page":page
         }]
	print dumps(input_json)
	
	insertIntoTable(dumps(input_json))

	
def imagesFromDirJSON( image_list, source_folder, collection ):
	json_images = []
	
	for image in image_list: 
        	name = os.path.basename(image)
		url = source_folder + "/" + collection + "/" + image
		alt = collection
		json_img = {"name":name, "url":url, "alt":alt }
		json_images.append(json_img)	
	
	return json_images
	

def insertIntoTable( input_json):
	try:
  		result = table.insert( json.loads(input_json) )
		print result	
	
	except client.errors.OperationFailure as e:
    		print "FAIL!"
		print e.code
    		print e.details

def searchForFilesAndInsert( images_loc, collection, author, site, start_page ):
	page = int(start_page) #logic here for checking if collection already exists
	source_folder = images_loc + "/" + collection
	count = 0
	images_list = []

	for file in os.listdir(source_folder):
    		if file.endswith(".JPG"):	
			if count == 6:
				buildJSONAndInsert( images_list, images_loc, collection, author, site, page)
				page += 1
				count = 0
				del images_list[:]
				images_list.append(file)
			else:
				count += 1
				images_list.append(file)

if __name__ == "__main__":
	author = "robyn graham"
	site = "robynwlp"
	folder = sys.argv[1]
	start_page = sys.argv[2]	

	searchForFilesAndInsert( "../img/out/", folder, author, site, start_page )
	print("done")



