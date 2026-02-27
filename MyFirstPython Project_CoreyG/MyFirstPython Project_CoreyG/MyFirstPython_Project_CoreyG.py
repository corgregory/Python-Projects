"""
This project will serve as a refresh to basic python syntax
, declaring variables and other basic statements
"""

# using the print function with a string literal
print("Hello, World!")
a = "Hello world!"
print(a.upper())
print(a.lower())
print(a.replace("H", "J"))

#print multiple statements on the same line
print("Hello, Ladies!", end="")
print("Hello Gentlemen!")
#printing integers
print(3 + 5)
print(8)
print(4*2)

# to give a variable a data type you have to cast it
x = str(5)
print(type(x))
x = int(5)
print(type(x))
x = float(5)
print(type(x))


#here is an example of unpacking in python

#declare a list with a variable name "fruit"
fruits = ["apples", "oranges", "peaches"]
x, y, z = fruits
print(x, end=" ")
print(y, end=" ")
print(z)

#Concatenation of Strings by declaring variables for strings and using the + for concatenating
a = "apples "
b = "and"
c = " oranges"
print(a + b + c)

#Here is an example of formatting strings (f-strings)
age = 35 
txt = f"My name is Corey, I am {age} years old."
print(txt)

#here is an example using a place holder and modifier
price = 25
print(price)
txt = f"The price is {price:.2f} dollars"
print(txt)



#use the isInstance() function to check the valuse stored in variable "X"
x = 250
print(isinstance(x, int))

#This is will be a list excercise sorting in ascending/descending order
MyVehicles = ["altima", "bronco", "volkswagon", "wrangler", "porsche", "corvette"]
print(MyVehicles)

#sort list in ascending order
MyVehicles.sort()
print(MyVehicles)
#print list in descending order
MyVehicles.sort(reverse = True)
print(MyVehicles)

#using a loop to print list
MyVehicles.sort()
for NewVehicleList in MyVehicles:
    print(NewVehicleList)

print("\n")

#use a loop with different syntax to print the list
MyVehicles.sort(reverse = True)
for i in range(len(MyVehicles)):
    print(MyVehicles[i])





