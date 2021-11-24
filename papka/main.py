import os  # для очистки экранаuser_choise == "1" and user_choise == "1" and
import potion_shop  # модуль продавца зелий
import gun_shop # магазин оружия
import arena  # арена


# создаем персонажа
user_name = "Вася Питонов" 
user_money = 5000
user_hp = 100
user_inventory = []
# главный цикл игры
# заканчивается с гибелью игрока или выходоми из игры
game = True
while game:
    # цикл выбора варианта действий
    # заканчивается выбором из предложенных вариантов
    user_choise = "0"
    while user_choise not in ("1", "2", "3", "4", "5"):
        os.system("cls")
        print(f"Вы начали игру!")
        print("------------")
        print(f"  имя: {user_name}")
        print(f"  деньги: {user_money}")
        print(f"  жизни: {user_hp}")
        print(f"  инвентарь:")
        for item in user_inventory:
            print("  •", item)
        print("------------")
        print(f" {user_name} сидит в лагере. Чем вы хотите заняться?")
        print("  1 — Зайти в лавку к алхимику")
        print("  2 — Пойти воевать на арену")
        print("  3 — Выйти из игры")
        user_choise = input(" Что делать? ")

    # проверки результата выбора

    # идем за зельями
    if user_choise == "1":
        result = potion_shop.show_location(user_name, user_money, user_inventory)
        user_money = result
    
    # идем воевать на арену
    if user_choise == "2":
        os.system("cls")
        result = arena.show_location(user_name, user_money, user_inventory)
        user_money = result

    # выходим из игры        
    if user_choise == "3":
        os.system("cls")
        print(f" {user_name} закончил игру")
        game = False

input(" ENTER — дальше")
