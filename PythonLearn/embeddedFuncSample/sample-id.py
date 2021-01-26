#!python3

a = 2
b = a
print("variable memory address")
print(id(a))
print(id(b))
print("primitive variable, but b is setted same memory addres of a! ")
print("in the case of Python, all variable is object, therefore, primitive variable also object.")
print("")
b = 4
print(str(a) + ":" + str(b))
print(id(a))
print(id(b))
print("When b is setted new value other with a, b is setted also a new memory address")
print("")

l1 = [1,2,3]
l2 = l1
l3 = l2[:]
print("object memory address")
print(id(l1))
print(id(l2))
print(id(l3))
print("")