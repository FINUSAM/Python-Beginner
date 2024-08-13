#45 * 3 = 555
#56+9 = 77
#856/6 = 4

#n1  = int (input("Enter Number 1 : "))
#opr = str(input("Enter Operation : "))
#n2  = int (input("Enter Number 2 : "))

#Using split() only because feels good. Could do it other way.	

n1, opr, n2 = input("Enter Question : ").split()

n1=int(n1)
n2=int(n2)

check = str(n1)+opr+str(n2)

if(check=="45*3"):
	res=(555)
elif(check=="56+9"):
	res=(77)
elif(check=="856/6"):
	res=(4)
else:
	if(opr=='+'):
		res = n1+n2
	elif(opr=='-'):
		res = n1-n2
	elif(opr=='*'):
		res = n1*n2
	elif(opr=='/'):
		res = n1/n2
	else:
		res="Somethings not right!"

input(res)