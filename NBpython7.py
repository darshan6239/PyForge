# #   FUNCTIONS
 
# #   Types
# """
# 1) Builtin 
# 2) User Defined 
# """

# #   1) No return type no Argument
# #         |in brackets we write arguments 
# def greet():
#     print("Hello User!")

# greet()


# #   2) No return type no Argument
# def greet1(name):
#     print("Welcome", name)
    
# name = input("Enter your name: ")
# greet1(name)

# #   3) With return type and without arguments 
# def get_no():
#     return 10**2

# #   1st way to take variable and print it and want to use value
# op  = get_no()  
# print(op)
# op += 2
# print(op)

# #   2nd direct use
# print(get_no())



# #   4) With return with argument 

# def cube (num):
#     return num**3

# num = int(input("Enter no: \n"))
# print(cube(num))

# op = cube(num)
# print(op)


# print("--------------------")
# #   *args = takes multiple input 
# def add1(*args):
#     print(sum(args))
#     print(type(args))

# add1(1,2,3,5765, 90)



# def info(name, age, marks):
#     return f"name:{name}\nage:{age}\nMarks:{marks}"

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# marks = float(input("Enter your marks: "))
# print(info(name,age,marks))



# Calculator 
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def div(a,b):
    print(a/b)


# print("===CALCULATOR===")
# while True:
#     ct = int(input("1. ADD\n2. SUBSTRACT\n3. MULTIPLY\n4. DIVISION\n5. EXIT "))
#     match ct:
#         case 1:
#             a = int(input("Enter 1st value: "))
#             b = int(input("Enter Second value: "))
#             add(a,b)

#         case 2: 
#             a = int(input("Enter 1st value: "))
#             b = int(input("Enter Second value: "))
#             sub(a,b)

#         case 3:
#             a = int(input("Enter 1st value: "))
#             b = int(input("Enter Second value: "))
#             multiply(a,b)

#         case 4:
#             a = int(input("Enter 1st value: "))
#             b = int(input("Enter Second value: "))
#             div(a,b)

#         case 5:
#             print("THANK YOU !")
#             break


result = 0
while True:
    if result is 0:
        result = float(input("Enter first number: "))

    print("1. Addition\n 2. Subtraction \n3. Division \n 4. Multiplication\n 5. Exit")
    choice = int(input("Enter choice: "))
            

    if choice == 5:
        print("Your Answer =", result)
        break

    num = int(input("Enter your next number: "))
    match choice:
        case 1:
            result += num
        case 2:
            result -= num

        case 3:
            if num == 0:
                print("Cannot divided by zero")
                continue
            result /= num
        case 4:
            result *= num

        case _:
            print("Invalid Output!")
            exit()
        
    print("Current Result =", result)
    cont = input("Continue with this result? (y/n): ")
    if cont == "n":
        print(f"Current Result: {result} ")

  