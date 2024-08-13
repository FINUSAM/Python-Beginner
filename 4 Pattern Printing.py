print("Enter no of rows : ", end="")
n = int(input())
print("Enter 1 or 0 : ", end="")
boolean = input()
print(end="\n")

if boolean=='0':
	i=1
	j=1
	while i<=n:
		while j<=i:
			print("*", end="")
			j=j+1
		i=i+1
		j=1
		print(end="\n")

if boolean=='1':
	i=1
	j=n
	while i<=n:
		while j>=i:
			print("*", end="")
			j=j-1
		i=i+1
		j=n
		print(end="\n")

input("\nPress Enter to Exit....")
