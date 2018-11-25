age = int(input("Please enter your age here:\n"))

try:
	y = age

except:
	print("Re-enter your age")

if ((y >= 1) and (y<=6)):
	print("Hi babby")
elif ((y>=6) and (y<=12)):
	print("Hey..kiddoo")
elif ((y>=13) and (y<=17)):
	print("Teens goes bananas")
elif ((y>=18) and (y<=40)):
	print("Go and VOTE!!!")
elif y>=41:
	print("Hola..UNCLE...perhaps AUNTY....")

	
	
	
