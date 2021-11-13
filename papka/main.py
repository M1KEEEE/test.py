import shop
from os import system

user_name = "Вася Питонов"
user_money = 5000
user_xp = 0
user_level = 1
user_inventory = []
user_inventory.append("меч")
user_inventory.append("конь")
user_inventory.append("щит")
game = true

def show_location_home(user_name, user_money, user_xp, user_level, user_inventory):
    while game:
    os.system("cls")
        print(f"имя:{user_money}")
        print(f"деньги:{user_money}")
        print("инвентарь:")
        for item in user_inventory:
            print("•", item)
        print("-------------------")
        print(f"{user_name} сидит на базе!")
        print(f"1 - пойти в магазин ")
        print(f"2 - уйти")

    user_choise = ""
    while user_choise not in ("1", "2"):
        user_choise = input("Что будем делать?")

# игра началась здесь
show_location_home()