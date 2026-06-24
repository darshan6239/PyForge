# For loop in python
# in c = for(inti; condition; update)

# in python = for variable in sequence:
"""                            string 
                                list
                                tuple
                                dictnumber --> range()"""

#   range (start, end + 1, step)
#for i in range(1,11,1):
 #   print(i)

"If you do not mention the start value then it is by default 0 "

# For printing the even numbers till 10 
for i in range(1,11):
    if i%2==0:
        print(i)
    
# Without if statement 
for i in range(0,11,2):
    print(i)


# to print from 51 to 60
for i in range(51, 61, 1):      # Always have +1 value at the end place 
    print(i)

#   reverse print
for i in range(10, 0, -1):
    print(i)

# 1 -10 even numbers addition between it

add = 0
for i in range(0,11,1):
    if i%2==0:
        add += i
print(f"The addition of the even numbers between 1-10 is {add}")

# 1 4 7 10 
for i in range(1, 11, 3):
    print(i)

#Homework 
#  Factorial of 7  -- User input 
#  21 x 1 = 21 .... 21 x 10 = 210
# A-Z
# a-z --> Vowels ( aeiou)
# 1-100 --> Total count print -- 100
# 23 - 1 --> reverse and print it in single line 


i = 7
fact = 1

while i > 0:
    fact = fact * i
    i -= 1

print(fact)

#  21 x 1 = 21 .... 21 x 10 = 210

i = 1 
while i<=10:
    print(f"21 x {i} = {21*i}")
    i += 1

# A-Z
for char in range(65, 91, 1):
    print(chr(char))

# a-z
for char in range(97,123,1):
    print(chr(char))

# a-z --> Vowels ( aeiou)
for char in range(97,123,1):
    ch = chr(char)
    if ch in "aeiou":
        print(chr(char))

# 1-100 --> Total count print -- 100

ct = 0
for i in range(1,101,1):
    ct += 1
print(f"The Final count is {ct}")

# 23 - 1 --> reverse and print it in single line 
for i in range(23, 0 , -1):
    print(i,end=" ")