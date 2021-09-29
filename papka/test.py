def show_main_location():
    print("Вы сидите в убежище")
    print("1 - пойти в казино")
    print("2 - подождать")

    user_choice = ""
    while user_choice not in ("1", "2"):
        user_choice = input("введите номер варианта и нажмите Enter ")

    if user_choice == "1":
        show_casino_location()
    else:
        print("Вы ждёте")
        show_main_location()


def show_casino_location():
    print("Вы попопали в казино")
    print("1 - оставить тут все деньги")
    print("2 - уйти")

    user_choice = ""
    while user_choice not in ("1", "2"):
        user_choice = input("введите номер варианта и нажмите Enter ")

    if user_choice == "1":
        show_pomoyka_location()
    else:
        print("Вы пошли в убежище")
        show_main_location()


def show_pomoyka_location():
    print("Вы остались без дома и денег")
    print("Проигрыш")


show_main_location()
input("Нажмите Enter для выхода")
