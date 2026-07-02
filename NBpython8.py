#   MODULES 

import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.ceil(45.01)) # Round off krke next value
print(math.floor(45.80))  # First value jo rahegi woh
print(math.pow(2,3))       # 2**3
print(math.pi)

calculate = 2*math.pi*2
print(calculate)

print("=====================================")

import random as r 
print(r.randint(1000,9999))     # OTP Methods
print(r.random())               # Generates value from 0.0 to 1.0
print(r.randrange(1,10,2))      # Odd printing 

x = ["red","black","blue","pink"]
print(r.choice(x))              # it is picking one color at a time 
print(r.choices(x, k=2))        # Choices will give you the more than one and if you want speicifc number then assign a key value

r.shuffle(x)                    # to shuffile the elements in the list 
print(x)

print("=====================================")
# Date time module 
import datetime
d = datetime.datetime.now()     # Overall 
print(d)
print(d.time())
print(d.day)
print(d.month)
print(d.year)



# date --> 2026/06/25
today_date = datetime.date.today()
print(today_date)

# after days 
after = today_date+ datetime.timedelta(days=5)
print(after)


dob = datetime.date(2000,10,10)
cd = datetime.date.today()
print(cd-dob)


print(cd.year-dob.year)

print("FOR USER ONE- ")
a= int(input("Enter your year: "))
b= int(input("Enter your month: "))
c= int(input("Enter your date: "))
dob1 = datetime.date(a,b,c)


print("FOR USER TWO- ")
d= int(input("Enter your year: "))
e= int(input("Enter your month: "))
f= int(input("Enter your date: "))
dob2 = datetime.date(d,e,f)

print(dob1 - dob2)

if dob1 > dob2:
    print("User 1 is greater")
elif dob1==dob2:
    print("Both are of same age! ")
else:
    print("User 2 is Greater")


