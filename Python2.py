# in, not in ,is 


#not in
print(45 not in x)
print(20 not in x)


x = [1,2,3]
print(x)
y=x
z =[5,6,7]
print(y)
print(x is y)
print(x is z)


# To print in one which is in two line 
print("Hello", end=" ")
print("World")

# Variable rules 
# 1. Should not start with numbers 
123age = 80  #  Error 
print(age123) 

#Should takea fter the name 
age123 = 80 #   Valid 

# 2. White spaces are not allowed 
city name ="Pune "  # Error!

# 3. Varibale name should not start with special characters except Underscore(_)
&name = "Ram"
print(&name)    # Error!



# Case Type :
#   1)CamelCASE 
countryName 
#      ^    - Last cahracter is uppercase 

#   2) Snakecase 
country_name

#   3) Pascal Case = Kitne bhi letters llikhe tab bhi characters ke first name should be upper case 
Country_Name


# Taking Inputs from users 
num = input("Enter Number: ")
print(num)

name = input("Enter Your Name: ")
print("Your name is:",name)


#Adding two numbers 
a = input("Enter 1st Number:")
b = input("Enter 2nd Number:")
print(a+b)    # --------1020 Coz Input function takes the input in str format

# so to avoid this we can use 
#       int()   float()     str()
a = int(input("Enter 1st Number:"))
b = int(input("Enter 2nd Number:"))
print(a+b)


#   Example 
a = int(input("Enter base Number:"))
b = int(input("Enter power Number:"))
print(a**b)


#   Example 
a = float(input("Enter 1st Number:"))
b = float(input("Enter 2nd Number:"))
print(a+b)

# If you've given the float value and you want it to print it in integers so 
a = float(input("Put a number: "))
print(int(a))


a = float(int(input("Put a number: ")))
print(a)





# Python follow indentation !! 

# if else 
num = int(input("Enter Number: "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")
    
#   Example 
num = int(input("Enter Age: "))
if num<18:
    print("Not Eligible for Voting")
else:
    print("Eligible for Voting")

#       Example
num = int(input("Enter Number: "))

if num%5 == 0 and num%7==0:
    print("Divisible")
else:
    print("Not divisible")


#   Example
a  = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

if a>b :
    print("1st is greater")
else:
    print("2nd is greater")


#   Example
ch = input("Enter Character: ")
if ch>= 'a' and ch<='z':
    print("LowerCase !")
else: 
    print("UpperCase !")


    
