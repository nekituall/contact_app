import time

import model_SQLlite as sql

def menu(user):
    """main menu func"""
    print(f"welcome {user}")
    var = int(input("Here are available commands: \n 1. Add contacts \n 2. List my contacts \n 3. Sort by \n"
                   " 4. Filter by \n 5. Search by name \n 6. Exit \n\nEnter command number:  "))
    while True:
        if var == 1:
            sql.add_contact(user)
            break
        elif var == 2:
            sql.select_all(user)
            break
        elif var == 3:
            sql.order_by(user)
            break
        elif var == 4:                #Допилить функцию фильтрации
            sql.select_where(user)
            break
        elif var == 5:
            # search_by_name(user)    #Допилить функцию поиска
            break
        elif var == 6:
            break
        else:
            print("Command not found!")
            case()
    time.sleep(1)   #Увеличить для чтения
    case()


def case():
    case = input("Exit program? : yes/no   ")
    if case == "yes" or case == "y":
        exit()
    else:
        menu(user)


if __name__ == '__main__':
    user = input('Welcome to contact_app! \nPlease sign in below \nLogin:  ')
    passw = input('Password:  ')
    menu(user)
