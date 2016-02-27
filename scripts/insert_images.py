from pymongo import MongoClient
from bson import Binary, Code
import os,json,sys
from bson.json_util import dumps
client = MongoClient()
db = client.robynwlp

from datetime import datetime

def buildGalleryJSON( source_folder, collection, photographer, website, page ):
	input_json = [{
                "images": imagesFromDirJSON( source_folder, collection, page ),
                "collection": collection,
                "photographer": photographer,
                "website": website
         }]
	print dumps(input_json)
	
	return dumps(input_json)

	
def imagesFromDirJSON( source_folder, collection, page ):
	json_images = []
	count = 0

	print(source_folder)
	print(collection)
	for file in os.listdir(source_folder):
    		if count == 6:
			page += 1
			count = 0
		else: 
			count += 1
		
		if file.endswith(".JPG"):
        		name = os.path.basename(file)
			url = file
			alt = collection
			json_img = {"page":str(page),"name":name, "url":url, "alt":alt }
			json_images.append(json_img)	
	#print(dumps(json_images))					
	return json_images
	

def insertIntoTable( table , input_json):
	try:
  		result = table.insert( json.loads(input_json) )
	
	except client.errors.OperationFailure as e:
    		print "FAIL!"
		print e.code
    		print e.details


if __name__ == "__main__":
	author = "robyn graham"
	site = "robynwlp"
	page = 1
	folder = sys.argv[1]
	

	gallery_json = buildGalleryJSON( "../out/" + folder,folder,author,site,page )
	insertIntoTable( db.gallery, gallery_json )
	print("done")



