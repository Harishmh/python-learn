import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


print(myclient.list_database_names())

#Check if "mydatabase" exists:

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database 'mydatabase' exists.")

  print(mydb.list_collection_names())

#Check if the "customers" collection exists:
  collist = mydb.list_collection_names()
  if "customers" in collist:
      print("The collection 'customers' exists.")


#Insert a record in the "customers" collection
mycol.insert_one(

    {
     "name": "John",
     "phone": "90808080-808",
     "address": "Highway 37"
     })

#Insert a record in the "customers" collection
"""
mydict = { "name": "Peter","phn": "8967680689",  "address": "Lowstreet 27" }

#print(x.inserted_id)

x = mycol.insert_one(mydict)

#print(x.inserted_id)

#Insert Multiple Documents

"""