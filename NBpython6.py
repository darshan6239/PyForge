#   SETS 
# it is unique
# Curly brackets 
# Unordered 
# Duplicate --> Unique IN NATURE (IT MEANS IT DO NO ALLOWS DUPLICATE ELEMENT IN PRINT)

x = {10,20}
print(type(x))
 
x = set()   # MANUAL INPUT 
x.add(10)   
print(x,type(x))


# LOOP
x = {10,20,30,40,10,20}
print(x)
for items in x:
    print(items) # FOLLOWS UNORDERED PAIRS


# FUNCTIONS & METHODS 
x.add(90)   # to add
print(x)

x.remove(40)    # if element not present it will throw an error
print(x)

x.discard(7)     # same as remove but if it did not get element it will not throw any error 
print(x)

x.pop()         # to remove any element from set
print(x)

x.clear()       # to clear all the set
print(x)

print("-----------------------")

a = {1,2}
b = a.copy()
print(b)


a.update([10,20,30])
print(a)


s = {10,80,99,50,30}
print(len(s), min(s), max(s), sum(s))
print("---------------")

# SET OPERATION
a = {1,2,3}
b = {3,4,5}
print(a.union(b))      # returns all but do not include any duplicate values
print(a|b)

print(a.intersection(b))    # Returns common value
print(a&b)

print(a.difference(b))      # Gives Differences between it
print(a-b)


print(a.symmetric_difference(b))    # Removes duplicate value 
print(a^b)


print("-----------------")
print("-----------------")

py_stud = {"ram", "sita", "komal", "ramu"}
jv_stud = {"ram", "pavan", "gita"}
fd_stud = {"gita", "komal", "payal"}

# 1. total count
all_students = py_stud | jv_stud | fd_stud
print("1. Total unique students :", len(all_students))

# 2. Students attending all 3 batches
all_three = py_stud & jv_stud & fd_stud
print("2. Students attending all 3 batches :", all_three)

# 3. Students attending only Java
only_java = jv_stud - py_stud - fd_stud
print("3. Only Java students :", only_java)

# 4. Students attending only Python
only_python = py_stud - jv_stud - fd_stud
print("4. Only Python students :", only_python)

# 5. Students not attending both Java and Python
java_python = py_stud | jv_stud
print("5. Students attending Java and Python :", fd_stud-java_python)

# 6. Count of students attending all 3 batches
count_three = len(py_stud & jv_stud & fd_stud)
print("6. Count of students attending all 3 batches :", count_three)

# 7. Name of student who attend only 1 batch at a time 
only_one = set()

for student in all_students:
    count = 0

    if student in py_stud:
        count += 1

    if student in jv_stud:
        count += 1

    if student in fd_stud:
        count += 1

    if count == 1:
        only_one.add(student)

print("7. Students attending only one batch :", only_one)




set1 = {12,35,8,25,5}
set2 = {25,6,35,15,8}

#   Divisible by 5
a = set1.union(set2)
for i in a:
    if i%5==0:
        print((i))

#   Even sum = ?
even_sum = 0
for i in set1:
    if i%2==0:
        even_sum += i
for i in set2:
    if i%2 == 0:
        even_sum += i
print(even_sum)
#   Common elements --> sum of it --> square of it --> and cube of it 
b = set1&set2
sum = 0
for i in b:
    sum = sum + i
print(sum)

sq = sum * sum
print(f"THe square is: {sq}")

cube = sq*sum
print(f"The cube is: {cube}")

#   Multiplication of Non repeating Numbers 
uni = set1^set2
print(uni)
mul = 1
for i in uni:
    mul = mul * i
print(f"The multiplication of unique numbersi :{mul}")




#   FROZEN SET
"""
immutable
unordered
hashing
"""
x = frozenset([1,2])
print(x, type(x))

roles = frozenset(["admin", "faculty", "recepist"])
for i in roles:
    if i=="admin":
        print(i)

        




