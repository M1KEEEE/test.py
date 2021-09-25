level = "0"
user_choise = ""
way1 = "0"
way2 = "0"
way3 = "0"

print("Вы находитесь у камня")
print("Выбирайте свой путь")
print("Налево пойти - 1")
print("Прямо пойти - 2")
print("Направо пойти - 3")

while user_choise not in("1", "2", "3"): 
    user_choise = input("Что вы выберете? ")

level = level +"1"

if level == "01":
    print("Дорога 1")
    print("Вы попали к разбойникам")
    print("У вас есть 3 варианта")
    print("Сделайте свой выбор")
    print("Варианты")
    print("1 - Сдаться")
    print("2 - Попытаться победить всех разбойников")
    print("3 - Пойти домой")

elif level == "02":
    print("Дорога 2")
    print("Вы заблудились в лесу")
    print("У вас есть 3 варианта")
    print("Сделайте свой выбор")
    print("Варианты")
    print("1 - Бродить по лесу в поисках выхода")
    print("2 - Сидеть и плакать")
    print("3 - Звать на помощь")

else: 
    print("Дорога 3")
    print("Вы нашли сундук с золотом")
    print("У вас есть 3 варианта")
    print("Сделайте свой выбор")
    print("Варианты")
    print("1 - Забрать всё золото себе")
    print("2 - Не брать золото")
    print("3 - Поделиться золотом с друзьями")

user_choise = ""
while user_choise not in("1", "2"): 
    user_choise = input("Что вы выберете? ")

level = level + user_choise
