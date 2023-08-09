name = input("What is your name? ")
age = input("What is your age? ")
print("Hello " + name + ", you are " + age + " years old!")

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")


string = input("Enter a string: ")
length = len(string)
print("The length of the string is:", length)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
print("The sum is:", sum)
print("The difference is:", difference)
print("The product is:", product)
print("The quotient is:", quotient)

password = input("Enter the password: ")
if password == "password123":
    print("Access granted")
else:
    print("Access denied")


year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")





# Numeric types
my_int = 10
my_float = 3.14
# Boolean type
my_bool = True
# Sequence types
my_list = [1, 2, 3, 4, 5]
# String type
my_string = "Hello, world!"










