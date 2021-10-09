import os
import random
import dice

user_name = "Вася"
user_money = 5000 

def create_user():
    user_name = "Вася"
    user_money = 5000 
    print("при создании персонажа у меня было", user_money)


def show_location_home():
    """
        Попадаем на начальную локацию - дом
    """
    os.system("cls")
    print("Вы дома")
    print("1 - в казино")
    print("2 - ждать")

    # спрашиваем у пользователя
    user_choice = ""
    while user_choice not in ("1", "2"):
        user_choice = input("введите номер варианта и нажмите Enter ")

    # проверяем ответ пользователя
    if user_choice == "1":
        show_location_casino()
    else:
        print("жду")
        os.system("cls")
        show_location_home()

def show_location_casino():
    """
        Попадаем на локацию казино
    """
    os.system("cls")
    print("Вы в казино")
    print("1 - домой")
    print("2 - ждать")
    print("3 - сыграть")

    # спрашиваем у пользователя
    user_choice = ""
    while user_choice not in ("1", "2", "3"):
        user_choice = input("введите номер варианта и нажмите Enter ")

    # проверяем ответ пользователя
    if user_choice == "1":
        show_location_home()
    if user_choice == "2":
        print("жду")
        os.system("cls")
        show_location_casino()
    if user_choice == "3":
        dice.play_dice(user_money)

# игра началась здесь
create_user()
show_location_home()
