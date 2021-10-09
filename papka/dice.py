import random
import main 
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
    elif user_dice == casino_dice:
        print("Ничья")
        print("У вас всё ещё", user_money, "денег")
        play_dice(user_money)
    else:
        user_dice < casino_dice
        print("Вы проиграли")
        user_money -= user_bet
        print("Теперь у вас", user_money, "денег")
    if user_money == 0:
        print("У вас закончились деньги")
        input("Нажмите ENTER чтобы вернуться в домой")
        main.show_location_home()
        user_money += 5000