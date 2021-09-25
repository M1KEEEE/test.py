level = "0"
user_choise = ""
way1 = "0"
way2 = "0"
way3 = "0"

print("Вы находитесь у камня")
print("Выбирайте свой путь")
print("1 дорога - ")
print("2 дорога - ")
print("3 дорога - ")

while user_choise not in("1", "2", "3"): 
    user_choise = input("Что вы выберете? ")

level = level +"1"

if level == "01":
    print("Дорога 1")
    print("У вас есть 3 варианта")
    print("Сделайте свой выбор")
    print("Варианты")
    print("1 - ")
    print("2 - ")
    print("3 - ")

elif level == "02":
    print("Дорога 2")
    print("У вас есть 3 варианта")
    print("Сделайте свой выбор")
    print("Варианты")
    print("1 - ")
    print("2 - ")
    print("3 - ")

else: 
    print("Дорога 3")
    print("У вас есть 3 варианта")
    print("Сделайте свой выбор")
    print("Варианты")
    print("1 - ")
    print("2 - ")
    print("3 - ")

user_choise = ""
while user_choise not in("1", "2"): 
    user_choise = input("Что вы выберете? ")

level = level + user_choise
