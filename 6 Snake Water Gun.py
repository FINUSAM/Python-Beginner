import random

choose = ['s', 'w', 'g']
counter=1
playerwins=0
computerwins=0
draws=0

while(counter<=10):

	computerChoice = random.choice(choose)
	playerChoice = input("Enter snake/water/gun : ")
	counter=counter+1

	if(computerChoice==playerChoice):
		print("Thats a DRAW!")
		draws=draws+1
	elif((computerChoice==choose[0] and playerChoice==choose[1]) or (computerChoice==choose[1] and playerChoice==choose[2]) or (computerChoice==choose[2] and playerChoice==choose[0])):
		print("Computer Wins!")
		computerwins=computerwins+1
	else:
		print("You Win")
		playerwins=playerwins+1

print(f"Total Games played : {playerwins+computerwins+draws}")
print(f"Games won by You : {playerwins}")
print(f"Games won by PC : {computerwins}")
print(f"Games drawn : {draws}")

