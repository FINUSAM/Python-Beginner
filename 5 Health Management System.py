def creatingfiles(client, option):
	#this fuction makes files if files are not present
	#used try except to ignore error files already exist
	try:
		temp = open(client+option+".txt", "x")
		temp.close()
	except Exception as e:
		print(end="")

def access():
	#this function asks user whether lock of retrieve
	#if the user enters wrong info, it will iterate itself till user corrects the mistake
	temp=""
	while(1==1):
		temp = input("Do you want to log or retrieve : ")
		if(temp=="log" or temp=="retrieve"):
			break
		else:
			print("Try Again, ", end="")
	return temp

def client():
	#this fuction ask user to select a client
	#if the user enters wrong info, it will iterate itself till user corrects the mistake
	temp=""
	while(1==1):
		temp = input("Choose any client (harry, rohan, hammad) : ")
		if(temp=="hammad" or temp=="rohan" or temp=="harry"):
			break
		else:
			print("Try Again, ", end="")
	return temp

def option():
	#this fuction ask user to choose between diet and exercise
	#if the user enters wrong info, it will iterate itself till user corrects the mistake
	temp=""
	while(1==1):
		temp = input("Choose diet or exercise : ")
		if temp=="diet" or temp=="exercise":
			break
		else:
			print("Try Again, ", end="")
	return temp

def retrieve(client, option):
	#this fuction allows user to print out data inside required file
	file = open(client+option+".txt")
	print(file.read())
	file.close()
	print("Retrieved Successfully")


def lock(client, option):
	#this fuction allows user to insert data to required file
	file = open(client+option+".txt", "a")
	tempstr=input(f"Enter the {option} : ")
	file.write(tempstr+"\n")
	file.close()
	print("Written Successfully")



############### Starting the Program ##############

access = access()
client = client()
option = option()
creatingfiles(client, option)

if access=="retrieve":
	retrieve(client, option)
elif access=="log":
	lock(client, option)
