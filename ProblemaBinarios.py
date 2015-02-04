def numeracion(numero):
	lista =[]
	lista2=[]
	lista3=[]
	for x in range(1,numero+1):
		lista.append(str(bin(x)))
		lista3.append(str(x))
	for num in lista:
		if impares(num) == False:
			lista2.append(num)
	print lista3 
	print lista 
	print lista2		

def impares(cad):
	numero = 0
	for i in cad[2:]:
		if (i == "1"):
			numero+=1
	if(numero % 2 != 0):
		return False
	return True			

print (numeracion(7))










# ProblemaBinarios
# ProblemaBinarios
#  ProblemaBinarios
