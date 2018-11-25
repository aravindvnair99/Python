def greet(lang):
	if lang=="en":
	    return "Hello"
	elif lang =="fr":
		return "Bonjour"
	elif lang=="hin":
		return "Namaste"

x = input("Enter language, en - english, fr - french, hin - hindi: ")

print(greet(x), "World")
