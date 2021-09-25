level = "0"
user_choise = ""
way1 = "0"
way2 = "0"
way3 = "0"

print("Вы находитесь у камня")
print("Выбирайте свой путь")
print("1 - ")
print("2 - ")
print("3 - ")

while user_choise not in("1", "2", "3"): 
    user_choise = input("Что вы выберете?")

level = level +"1"

if level == "01":
    print("дорога 1")
    print("Сделайте свой выбор")
    print("Варианты")
    print("1 - ")
    print("2 - ")
    print("3 - ")

elif level == "02":
    print("дорога 2")
    print("Сделайте свой выбор")
    print("Варианты")
    print("1 - ")
    print("2 - ")
    print("3 - ")

else: 
    print("дорога 3")
    print("Сделайте свой выбор")
    print("Варианты")
    print("1 - ")
    print("2 - ")
    print("3 - ")

user_choise = ""
while user_choise not in("1", "2"): 
    user_choise = input("Что вы выберете?")

level = level + user_choise
