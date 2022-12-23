
import model_SQLlite as sql

def menu(user):
    """main menu func"""
    print(f"welcome {user}")
    var = int(input("Here are available commands: \n 1. Add contacts \n 2. List my contacts \n 3. Sort by \n"
                   " 4. Filter by \n 5. Search by name \n 6. Exit \n\n Enter command number:  "))
    while True:
        if var == 1:
            add_contact(user)
            break
        elif var == 2:
            list_all(user)
            break
        elif var == 3:
            sort_by(user)
            break
        elif var == 4:
            filter_by(user)
            break
        elif var == 5:
            search_by_name(user)
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


def add_contact(user):
    "Function to add contact into DB, no checks for input data"
    try:
        while True:
            print("Please fill in contact info:")
            surname = input("Type in Surname:  ")
            name = input("Type in Name:  ")
            secname = input("Type in Second name:  ")
            company = input("Type in company name:  ")
            job = input("Type in job:  ")
            email = input("Type in email:  ")
            tel = input("Type in phone number:  ")
            contact = [surname, name, secname, company, job, email, tel, "valid", user]
            choice = input(f"{contact} \nis this info correct? yes/no:     ")
            if choice == "yes" or choice == "y":
                sql.insert_contact(contact)
                print("Contact has been added")
                add = input("Add more contact? yes/no:      ")
                if add != "yes" or "y":
                    break
            else:
                print('Okay, Let`s try again')
    except Exception as e:
        print(f"{e} occured")


def case():
    case = input("Exit program? : yes/no   ")
    if case == "yes" or case == "y":
        exit()
    else:
        menu()








if __name__ == '__main__':
    user = input('Welcome to contact_app! \nPlease sign in below \nLogin:  ')
    passw = input('Password:  ')
    menu(user)
