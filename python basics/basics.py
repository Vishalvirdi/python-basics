name = "Vishal"
age = 23
pi = 3.14
array = [1, 2, 3, 4, 5]
# print("My name is", name, "and I am", age, "years old" )
# # print("My age is", age) 
# print("The value of pi is", pi)
# print("The array is", array)

# print(type(name))
# print(type(age))
# print(type(pi))
# print(type(array))

# number = int(input("Enter a number: "))
# print("The number is", number)
# if number%2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# a = 10
# b = 20
# print(b/a)
# print(b//a)
# array  = [1, 2, 3, 4, 5]
# for i in array:
#     print(i)

# def add(a, b):
#     return a + b

# print(add(1, 2))


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    print("The sum is", number1 + number2)
elif operation == "-":  
    print("The difference is", number1 - number2)
elif operation == "*":
    print("The product is", number1 * number2)
elif operation == "/":
    print("The quotient is", number1 / number2)
else:
    print("Invalid operation")