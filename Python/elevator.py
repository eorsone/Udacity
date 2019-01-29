import time
def print_pause(string):
	print (string)
	time.sleep(1.0)

def intro():
	print_pause("You have arrived at your new job!")
	print_pause("You are in the elevator")

def first_floor(items):
	print_pause("You push the button for the first floor.")
	print_pause("After a few moments, you find yourself in the Lobby")
	if "ID card" in items:
		print_pause("The clerk greets you, but she has already given you your" 
					" ID card, so there is nothing more to do here now")
	else:
		print_pause("The clerk greets you and gives you your ID card")
		items.append("ID card") 
	print_pause("Where would you like to go next?")
	option(items)

def second_floor(items):
	print_pause("You push the button for the second floor.")
	print_pause("After a few moments, you find yourself in the Human Resource Department.")
	if "handbook" in items:
		print_pause("The HR folks are busy at their desks.")
		print_pause("There doesn't seem to be much to do here.")
	else:
		print_pause("The head of HR greets you")
		if "ID card" in items:
			items.append("handbook")
			print_pause("He looks at your ID card and then gives " 
						"you a copy of the employee handbook.")
		else:
			print_pause("He has something for you, but says he can't " 
						"give it to you until you go get your ID card.")
	print_pause("Where would you like to go next?")
	option(items)

def third_floor(items):
	print_pause("You push the button for the third floor.")
	print_pause("After a few moments, you find yourself in the Engineering Department")
	print_pause("This is where you work!")
	if "ID card" in items:
		print_pause("You use your ID card to open the door.")
		print_pause("Your program manager greets you and tells you that you need to have " 
					"a copy of the employee handbook in order to start work.")
		if "handbook" in items:
			print_pause("Fortunately, you got that from HR!")
			print_pause("Congratulatons! You are ready to start your new job "
							"as vice president of engineering!")
		else:
			print_pause("They scowl when they see that you don't have it, and send you back to the elevator.")

	else:
		print_pause("Unfortunately, the door is locked and you can't get in.")
		print_pause("It looks like you need some kind of key card to open the door.")
		print_pause("You head back to the elevator")	
	print_pause("Where would you like to go next?")
	option(items)

def option(items):
	print_pause("Please enter the number for the floor you would "
				"like to visit:")
	floor = (input("1. Lobby\n"
				"2. Human Resources\n"
				"3. Engineering Department\n"))
	if floor == "1":
		first_floor(items)
		
	elif floor == "2":
		second_floor(items)
		
	elif floor == "3":
		third_floor(items)
	print_pause("Sorry, I do not understand.")
	option()

def play_game():
	items = []
	intro()
	option(items)
play_game()