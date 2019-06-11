def main():
    while (1):
        # chossing option to do CRUD operations
        selection = raw_input('\n Select 1 to insert, 2 to update, 3 to delete\n')

        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            delete()
        else:
            print
            '\n INVALID SELECTION \n'