def hello(name):
	
	print("hello world "+name)


def factorial(n):
	if n == 0:
		return 1


	return n*factorial(n-1)

#this is a comment
name = input("enter your name : ")
hello(name)


# this is a comment

num    =   int(input("enter number to calculate factorial : "))
fac     =     factorial(num)
# this is a comment
# this is a comment# this is a comment# this is a comment


print(     "  factorial    of   "   +   str(  num  ) +  "  is",fac)