#   12/06/2026
#   Pallindrome 
#   ORG == REV 
#   slicing[S1:[-]:STEPS]
#         {Start index: end index : stepping}

X = "India"
print(X[1:4])
print(X[0:5:2])

x = "India is my country!"
print(x[6:8])
print(x[12:17])
print(x[7:10])
print(x[16:])
print(x[-10:-15:-1])

print(x[17:10:-1])

# Palindrome function

x = input("Enter any number to check wheather it is palindrome or not: ")
if x == x[::-1]:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")


# New Example 

x = "abc1234"
ct_digit = 0
ct_char = 0

for ch in x:
    if ch >= '0' and ch <= '9':
        ct_digit += 1
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        ct_char += 1

print(ct_digit)
print(ct_char)

# for ASCII value we we'll use "ORD" function which convert CHaracter to ASCII value and for ASCII to CHaracter we we'll use "CHR"

# C - c
print(ord("C"))
print(chr(ord('C')+32))

x = "hello"
new_str = ""
for i in x:
    if i >= 'a' and i<= 'z':
        new_str += chr(ord(i)-32)
print(new_str)

# sWapCaSe --> swapcase
x = "sWapCaSe"
new_str = ""

for i in x:
    if i >= 'a' and i <= 'z':
        new_str += chr(ord(i) - 32)  
    if i >= 'A' and i <= 'Z':
        new_str += chr(ord(i) + 32)  
print(new_str)
    

#Another programming

x = "programming"
# even char
for i in x:
    if ord(i)%2 == 0:
        print(i,ord(i))


# to remove duplicates from string & to print the duplicates in the string
x = "programming"
unique = ""
for ch in x:
    if ch not in unique:
        unique += ch
print(unique)


# to remove the spacing in the the sentence 
x = "I like python programming" # we have to count the characters in x but spacing has indexing which disturb the count
ct = 1
for ch in x:
    if ch != " ":
        ct += 1
print(ct)

# to count space
x = "I like python programming" 
ct = 0
for ch in x:
    if ch == " ":
        ct += 1
print(ct)


