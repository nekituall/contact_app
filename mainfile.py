

def menu(login):
    """main menu func"""
    print(f"welcome {login}")
    var = int(input("Here are available commands: \n 1. Modify contacts \n 2. List my contacts \n 3. Sort by \n"
                   " 4. Filter by \n 5. Search by name \n 6. Exit \n\n Enter command number:  "))
    while True:
        if var == 1:
            modify()
            break
        elif var == 2:
            list_all()
            break
        elif var == 3:
            sort_by()
            break
        elif var == 4:
            filter_by()
            break
        elif var == 5:
            search_by_name()
            break
        elif var == 6:
            break
        else:
            print("Command not found!")
            case()

    print("end of menu")


# def menu(user):
#     """main menu func"""
#     print("Here is a list of available commands: \n 1. List all \n 2. Sort by \n 3. Filter by \n 4. Search by name \n "
#           "5. Exit")
#
#     print("end of menu")


def modify():
    var = int(input("Here are available commands: \n 1. Add  \n 2. Modify \n 3. Delete "))
    while True:
        if var == 1:
            add_contact(user)
            break
        elif var == 2:
            modify_contact(user)
            break
        elif var == 3:
            del_contact(user)
            break
        else:
            print("No such command! Re-enter")





def case():
    case = input("Exit program? : yes/no   ")
    if case == "yes" or case == "y":
        exit()
    else:
        menu()








if __name__ == '__main__':
    login = input('Welcome to contact_app! \nPlease sign in below \nLogin:  ')
    passw = input('Password:  ')
    if login == "admin" and passw == "admin":
        admin_menu(login)
    else:
        menu(login)
