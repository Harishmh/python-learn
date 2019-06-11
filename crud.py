import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

from pymongo import MongoClient

def insert():
    try:
        name = input("\nEnter name :\n")
        phone_number = input("\nEnter phone_number :\n")
        address = input("\nEnter address:\n")

        mycol.insert_one(
        {
            "name": name,
            "phone": phone_number,
            "address": address,

        })
        print("\nInserted data successfully\n")
    except NameError:
        print("Error!")

# function to read records from mongo db
def read():
    try:
        x = mycol.find()
        print("\n All data from user Database \n")
        for emp in x:
            print(emp)

    except NameError:
        print("Error!")

def update():
    try:
        #criteria = input("\nEnter id to update\n")
        name = input("\n Enter name to update\n")
        phone_number = input("\nEnter phone number to update\n")
        address = input("\nEnter addrees to update\n")

        mycol.update_one(
            {"name": name},
            {
                "$set": {

                    "phone": phone_number,
                    "address": address
                }
            }
        )
         #print("\nRecords updated successfully\n")
    except NameError:
        print("An exception occurred")

def delete():
    try:
        criteria = input("\nEnter name  to delete\n")
        mycol.delete_many({"name": criteria})
        print("\n deletion successfull")
    except NameError:
        print("An exception occured")

while 1:

    # choosing option to do CRUD operations
    selection = int(input("\n Enter 1 to insert,2 to Read, 3 to update, 4 to delete: \n"))
    if selection == 1:

        print("you are trying to insert ")
        insert()
        break
    elif selection == 2:
        print("Read Data")
        read()
        break
    elif selection == 3:
        print("Updating Data")
        update()
        break
    elif selection == 4:
        print("deeleting Data")
        delete()
        break
    else:
        print("INVALID SELECTION")
        break

