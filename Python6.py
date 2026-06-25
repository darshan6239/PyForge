#   NUMBERS PROGRAM 

"GIVEN THAT THERE IS NUMBER 1234 = WE WANT THE SUM OF THIS NUMBER"

num = 1234
sum = 0
while num > 0:
    rem = num%10
    sum = sum + rem
    num = int(num/10) # or else can be written as num//10
print(sum)


# reverse the number 
num = 4321
rev = 0
while num > 0:
    rem = num%10
    rev = (rev*10)+rem;
    num//=10
print(rev)

# Number given is 121 and reverse is 121 = palindrome number 

num = int(input("Enter any number: "))
temp = num
rev = 0
while num>0:
    rem = num%10
    rev = (rev*10)+rem
    num = num//10
    
if temp==rev:
    print("The given number is palindrome ")
else:
    print("Not Palindrome")



#   Factors of 6
num = 6
i = 1
while i<=num:
    if num%i==0:
        print(i, end=" ")
    i+=1

