# # 15/06/2026
# s = "hello"
# a = sorted(s)
# print(a)
# b = "".join(a)  # to sort the word without in list ! 
# print(b)

# #   LIST
# """ 
# List has itself indexing 
# 0 index
# 1 start 
# list is mutable in nature and we can change it (string is immutable)
# allows duplicate value
# Heterogenous ( can pass similar values and can pass different values )

# """ 

# # List inbuild method is ---- append() to add element in the list

# x = ["darshan", 45, "Pranav", 25, "Aditya", 18, "virag", 7]
# x.append("Hello")
# print(x)



# # add element by taking user ip
# x = []
# print(x)
# for i in range(5):
#     ip = input(f"Enter Element {i+1}: ")
#     x.append(ip)
# print(x)


# # Extend() function (To use to expand the existing list !)
# x = [1,2]
# print(x)
# x.extend([3,4])
# print(x)


# # insert(index, value)
# x = [11,13]
# x.insert(1,12)
# print(x)

# # remove(element)/pop(index)
# x = [10,8,9,"hi",90,89]
# x.remove("hi")
# x.pop(4)
# print(x)
# x.clear()   # clears all the list
# print(x)




# # List operations 

# x = [10,20,40,60,10,30]
# print(x.count(10))
# print(x.index(30))

# x.sort()
# print(x)

# x.reverse()
# print(x)

# y = x.copy()
# print(y)



# # Function 
# x = [78, 90,12,8]
# print(len(x))
# print(max(x)) # runs only when all are numbers in list
# print(min(x))
# print(sum(x))
# print(sorted(x,reverse=True))

# # SUm without inbuilt function
# x = [10,20,45,30]
# sum = 0
# for i in x:
#     sum = i + sum
# print(sum)



# # Find the greater element in list without inbuilt function

# x = [10,20,30,40]
# max_val = 0
# for i in x:
#     if max_val < i:
#         max_val = i
# print(max_val)


student = [1, "ram", 45, 2, "Sita", 78, 3, "pOOJA", 90]
names = []
index = []
marks = []

for i in range(0,9,3):
    index.append(student[i])
    names.append(student[i+1])
    marks.append(student[i+2])


print(marks)
print(index)
print(names)











