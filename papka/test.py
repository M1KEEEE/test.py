def show_main_location():
    print("\nВы сидите в убежище\n")
    print("1 - пойти в казино")
    print("2 - подождать\n")

    user_choice = ""
    while user_choice not in ("1", "2"):
        user_choice = input("введите номер варианта и нажмите Enter ")

    if user_choice == "1":
        show_casino_location()
    else:
        print("Вы ждёте")
        show_main_location()


def show_casino_location():
    print("\nВы попопали в казино\n")
    print("1 - играть")
    print("2 - уйти\n")

    user_choice = ""
    while user_choice not in ("1", "2"):
        user_choice = input("введите номер варианта и нажмите Enter ")

    if user_choice == "1":
        show_pomoyka_location()
    else:
        print("Вы пошли в убежище\n")
        show_main_location()


def show_pomoyka_location():
    print("\nВы проиграли и остались без дома и денег")
    print("Проигрыш\n")


show_main_location()
input("Нажмите Enter для выхода")
