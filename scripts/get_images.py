from pymongo import MongoClient
import sys

client = MongoClient()
db = client.robynwlp

def getCollection(collection):
	cursor = db.gallery.find({"collection": collection})
	for document in cursor:
    		print(document)

def getCollectionPage(collection, page):
        cursor = db.gallery.find( {'collection':collection,'page':page},{'_id':0} )
        
	for document in cursor:
                print(document)
	
	if document is None:
		return None
	else:	
		return document



if __name__ == "__main__":
#	getCollection(sys.argv[1])
	print("go")
    	getCollectionPage(sys.argv[1],int(sys.argv[2]))
