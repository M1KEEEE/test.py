level = "0"
user_choise = ""

print("У камня")
print("1- ")
print("2- ")
print("3- ")

while user_choise not in("1", "2", "3"): 
    user_choise = input("Что вы выберете?")

level = level +"1"

if level == "01":
    print("дорога 1")
    print("На вас напали")
    print("Варианты")

elif level == "02":
    print("дорога 2")

else: 
    print("дорога 3")

user_choise = ""
while user_choise not in("1", "2"): 
    user_choise = input("Что вы выберете?")

level = level + user_choise
