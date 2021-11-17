"""
TODO:
сделать персонажа словарем
вынести функцию показа персонажа в отдельный модуль
вынести функцию выбора вариантов в отдельный модуль
придумать систему диалогов
"""

import os  # для очистки экрана
import shop  # модуль продавца зелий


# создаем персонажа
user_name = "Вася Питонов"
user_money = 5000
user_hp = 100
user_luck = 1
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
        print(f"имя: {user_name}")
        print(f"деньги: {user_money}")
        print(f"жизни: {user_hp}")
        print(f"удача: {user_luck}")
        print(f"инвентарь:")
        for item in user_inventory:
            print("•", item)
        print("----------")
        print(f"{user_name} сидит у костра в лагере. Отсюда можно отправиться в разные места.")
        print("1 — Зайти в лавку к алхимику")
        print("2 — Выйти из игры")
        user_choise = input("Что делать? ")

    # проверки результата выбора

    # идем за зельями
    if user_choise == "1":
        result = shop.show_location(user_name, user_money, user_inventory)
        user_money = result
    
    # выходим из игры        
    else:
        print(f"{user_name} закончил игру")
        game = False

    input("ENTER — дальше")
