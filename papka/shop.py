from os import system
import main

def show_location_shop(user_name, user_money, user_inventory):
    is_busy = True
    while is_busy:
        system("cls")
        potion_price = 500
    if user_choise == "1" and user_money >= potion_price:
        user_money -= potion_price
        user_inventory.append("зелье")
    elif user_choise == "1" and user_money < potion_price:
        is_busy = False
        print("Не хватает денег!")
        input("ENTER - чтобы продолжить")
        return user_money