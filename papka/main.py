import os
import random

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
        play_dice(user_money)


def play_dice(user_money):
    print("Сейчас у вас", user_money, "денег")
    user_dice = random.randint(2, 12)
    casino_dice = random.randint(2, 12)
    user_bet = int(input("Сколько вы хотите поставить? "))

    #роверка наличия денег
    if user_bet > user_money:
        print("У вас нет столько денег!")
        play_dice(user_money)

    #проверка привильности ставки
    if user_bet <=0:
        print("Вы не можете поставить так мало!") 
        play_dice(user_money)
    else:
        print(f"Вы бросили кости, выпало {user_dice}")
        print(f"Казино кости, выпало {casino_dice}")

    if user_dice > casino_dice:
        print("Вы победили")
        user_money += user_bet
        print("Теперь у вас", user_money, "денег")
        play_dice(user_money)

    if user_dice < casino_dice:
        print("Вы проиграли")
        user_money -= user_bet
        print("Теперь у вас", user_money, "денег")
    if user_money == 0:
        print("У вас закончились деньги")
        input("Нажмите ENTER чтобы вернуться в домой")
        show_location_home()
    else:
        play_dice(user_money)

    if user_dice == casino_dice:
        print("Ничья")
        print("У вас всё ещё", user_money, "денег")
        play_dice(user_money)

    if user_money == 0:
        print("У вас закончились деньги")
        input("Нажмите ENTER чтобы вернуться в домой")
        show_location_home()
        user_money += 5000
    else:
        play_dice(user_money)


# игра началась здесь
create_user()
show_location_home()
