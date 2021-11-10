import os


user_name = "Вася Питонов"
user_money = 1000
user_inventory = []

def show_location_shop(user_name: str, user_money: int, user_inventory: int, user_choise):
	is_shopping == True
	potion_price = 100
	while is_shopping:
		os.system("cls")
		print(f"{user_name} зашел в лавку алхимика Варенцова. У него можно купить зелья со странным запахом.")
		print(f"1 - купить зелье за {potion_price}")
		print(f"2 - уйти")

		user_choise = "0"
		while user_choise not in ["1", "2"]:
			user_choise = input("Что будем делать?")

		if user_choise == "1" and user_money >= potion_price:
			user_money -= potion_price
			user_inventory.append(potion)
			print(f"{user_name} купил зелье")
		elif user_choise == "1":
		elif
		else:
			is_shopping = False



show_location_shop(user_name, user_money, user_inventory)
