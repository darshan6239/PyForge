# Adding the element's ! to the list 
x = [1,2]
y = [3,4]

print("Previous-",x)
x.extend(y)
print("After Extend-",x)

#using index element we canhave the particular element from the list 
print(x.index(2))

#Reverse 
x = [12, 34, 56 , 20]
x.reverse()
print(x)

#Copying in list 
a = [10,20]
b = a.copy()
print(b[0])


#AScending format
x = [90,70,50,100,30]
x.sort()
print(x)

#For descending order
x.sort(reverse=True)
print(x)

#Counting 
x = [11, 33, 444, 11 , 22]
print(x.count(11))


"""     FUNCTIONS       """

x = [10, 40, 20, 30]
print(max(x))
print(min(x))
print(sum(x))
print(len(x))



# Print the sum without inbuilt functions 
x = [10, 20 , 30 ,40]
sum = 0
for i in x:
    sum = sum + i
print(sum)

#   Extract the maximum function from the list
x = [10, 20 , 30 ,40, 80, 10]
max = 0
for i in x:
    if i>max:
        max = i
print(max)



# Assign the zero without builtin functions 
# Simple 
x = [10, 20 , 30 ,40, 80, 10, 100]
x[-1] = 0
print(x)

# Using using the built in functions 

""" 
for i in range(len(x)):
    print(i)   ---> Returns index value 
    print(x[i]) --> Returns value at the index 

            """
x = [10, 20, 30, 40, 80, 10, 100]

for i in range(len(x)):
    if x[i] == 30:
        x[i] = 0
print(x)


# Using the built in function
x = [20,30,10]
print(x[::-1])

# without using built in functiins 
x = [20, 30, 10]
rev = []
for i in range(len(x)-1,-1,-1):
    rev.append(x[i])
print(rev)

# Unique array ! 
x = [21, 23, 24, 21, 25]
unq_elements=[]
for i in x:
    if i not in unq_elements:
        unq_elements.append(i)
print(unq_elements)


