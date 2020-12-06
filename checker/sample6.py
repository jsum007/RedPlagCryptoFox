import numpy as np

def hello(name):
	print("hello world "+name)
	print("hello everyone")
	print("hello neighbours")
	hello(name)


def factorial(n):
	if n == 1:
		return 1
	return n*factorial(n-1)

#this is a comment
name = input("enter your name : ")#this is a comment
hello(name)

num = int(input("enter number to calculate factorial : "))
fac = factorial(num)
print("factorial of "+ str(num) + " is",fac)
x = lambda a:a+10.2
print(x(4))