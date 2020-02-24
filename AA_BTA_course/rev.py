"""def tuple_fun(tple):
		return print( tple+tple)

tuple_fun((1,2,"s"))
"""

b=230

def fun1():
	a=20
	print(a)

def fun2():
	b=30 #local variable of fun2
	print(b)


fun1()
fun2()
print(b)#global variable
