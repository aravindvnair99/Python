x=input("Enter language, en -english, fre-french, hin -hindi")

def greet(lang):
	if lang=="en":
		print("Hello")
		
	elif lang =="fre":
		print("Bonjur")
		
	elif lang=="hin":
		print("NAMASTEE")

print(greet(x),  "WORLD")
