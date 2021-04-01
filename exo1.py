
#!/usr/local/bin/python3.9

def convert(T):
	t=T[:-2] #enlève les 2 derniers caractères donc la lettre
	T=T.lower()
	
	if T[-1] =="f":  #récupére le dernier caractère de T
		c=(5/9)*(int(t)-32)
		print("la température est de "+str(c)+ " °C")

	else:
		f=int(t)*(9/5)+32
		print("la température est de "+str(f) + " °F")

# test
test=input("Tapez une température avec son unité (°C/°F): ")
convert(test)
