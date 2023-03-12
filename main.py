print("Welcome to the simple calculator")
a = int(input("Enter a value: "))
b = int(input("Enter another value: "))
c = input("Enter add, sub, mul, or div: ")

if c == ("add"):
	sum = (a+b)
	print("The answer is: ", sum)
elif c == ("sub"):
	sub = (a-b)
	print("The answer is: ", sub)
elif c == ("mul"):
	mul = (a*b)
	print("The answer is: ", mul)
elif c == ("div"):
	div = (a/b)
	print("The answer is: ", div)
else:
	print("I can't understand, please try again.")