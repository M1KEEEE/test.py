import os
import arena

def show_location(user_name, user_money, user_inventory):
    is_in_potion_shop = True
    potion_cost = 100 # стоимость зелья
    potion_prise = 0 # цена за все зелья
    potion = 0

    # главный цикл модуля
    # заканчивается, если игрок выберет вернуться в лагерь
    while is_in_potion_shop:

        # печатаем инфу о месте и игроке
        # предлагаем игроку выбор действий
        user_choise = "0"

        while user_choise not in ("1", "2") and user_money > 0:
            os.system("cls")
            print(f" {user_name} зашел в лавку алхимика.")
            print("------------")
            print(f"  деньги: {user_money}")
            print(f"  инвентарь:")
            for item in user_inventory:
                print("  •", item)
            print("----------")
            print(f"  1 — Купить зелье за {potion_cost}")
            print("  2 — Вернуться в лагерь")
            user_choise = input(" Что делать? ")


        # проверяем выбор игрока

        # пытаемся купить зелье, денег хватает
        if user_choise == "1":
            potion_quantity = int(input(" Сколько зелий вы хотите купить? ")) # справшиваем количество зелий
            potion_prise = potion_quantity * potion_cost
            user_money -= potion_prise
            potion += potion_quantity
            user_inventory.append(f"зелье x {potion}")
            is_in_potion_shop = True
            
        elif user_choise == "1" and user_money < potion_prise:
            print(f" У {user_name} не хватает денег.")
            is_in_potion_shop = True
            input()

        elif user_choise == "2" and user_money > 0:
            print(f"{user_name} вернулся в лагерь")
            is_in_potion_shop = False
            game = True
            input("ENTER — дальше")



    # мы не возвращаем инвентарь, он изменяемый объект и изменяется прямо в этом модуле
    return user_money
