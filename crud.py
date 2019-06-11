import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

def insert():
    try:
        name = input("Enter name :")
        phone_number = input("Enter phone_number :")
        address = input("Enter address:")

        mycol.insert_one(
        {
            "name": name,
            "phone": phone_number,
            "address": address,

        })
        print("\nInserted data successfully\n")
    except NameError:
        print("Error!")


while 1:

    # choosing option to do CRUD operations
    selection = int(input("\n Enter 1 to insert, 2 to update, 3 to delete: \n"))
    if selection == 1:

        print("one")
        insert()
    elif selection == 2:
        print("two")
        #update()
    elif selection == 3:
        print("three")
        #delete()
    else:
        print("INVALID SELECTION")

# Function to update record to mongo db
