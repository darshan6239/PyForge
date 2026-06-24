# for increment in c we use ++ in pyhton we define it like example a = 10 , a+=2

i = 1
while i<=3:
    print("Hello World")
    i += 1



i = 1
while i<= 10:
    print(i)
    i += 1


# Odd Numbers --> 1,3,5,7,9...
i = 1
while i<= 10:
    if(i%2!=0):
        print(i)
    i+=1

# Even Numbers == 
i =1
while i<=10:
    if(i%2==0):
        print(i)
i+=1

i = 0
while i<= 10:
    print(i)
    i+=2

# For reverse numbering
i = 10
while i>=1:
    print(i)
    i -= 1


# Sum of Numbers 

i = 1
sum = 0
while i<=20:
    sum += i
    i+=1
print("Sum is: ",sum)


# Sum of even numbers 

i = 1
sum = 0

while i <= 50:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1  
print("Sum is:", sum)


# Even and odd in one 
i = 1
sum = 0
Oddsum = 0

while i <= 50:
    if i % 2 == 0:
        sum = sum + i
    else:
        Oddsum = Oddsum + i
    i = i + 1  

print("Sum is:", sum)
print("Sum of Odd is:", Oddsum)

print("Total =", sum + Oddsum)


# 1 --> 100 filter it and divisble by 5 and 7 

# Print table of 5
i = 1

while i <= 10:
    print("5 x", i, "=", 5 * i)
    i += 1


# Print A-Z  
# So we can print using ASCII value and inbuilt functions
# ord() --> a --> ASCII
# chr() --> ascii --> Char
i = 65
while i<=92:
    print(chr(i))
    i+= 1


# Reverse z - a
# Aplhabets --? ACEGI Diff of 2
# EVen alphabets -- ASCII
# 1 - 10 --> Square 
# 1 - 50  ( %3 cube, % 9 = square, % 2 and %4 == no 6 )