import random
from os import system

secret = random.randint(1, 99)
max_guess = 9


while(True):
	while max_guess>0:
		print("\nYou have {} guesses remaining".format(max_guess))
		userinput = int(input("\nGuess the Number : "))
		if userinput > secret:
			system('cls')
			print("It's too big")
			max_guess-=1
			continue
		elif userinput<secret:
			system('cls')
			print("It's too small")
			max_guess-=1
			continue
		else:
			break

	if max_guess==0:
		print("\nYour Guesses are Over......")
	else:
		print("\nYou Found the Right Answer......")

	play_again_input = input("\nDo you want to play again ? ")

	if(play_again_input=='n'):
		break
	else:
		max_guess=9;