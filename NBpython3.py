#   16/06/2026
x = [10,20,20,30,40,50,60]
# flag = 0
# ip = int(input("Enter the key you want to find: "))
# for i in x:
#     if ip == i:
#         print("FOund")
#         flag=1
# if flag == 0:
#         print("Not found")


#   DUPLICATES IN THE LIST
x = [10,20,25,90,20,30,40,40,50,98,98,60,0,0]
# print(x)
# print("Duplicate values are : ")
# y = []
# for i in x:
#     if x.count(i)>1 and i not in y:
#         print(i)
#         y.append(i)


# #   UNIQUE ELEMENT remove
# unique = []
# for i in x:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# To print unique element
# print(x)
# print("Unique Element: ")
# for i in x:
#     if x.count(i)<=1:
#         print(i)


# Sorting without function 


# even odd 
x = [1,2,3,4,5,6,7,8,9]
for i in range(len(x)):
    if i%2==0:
        x[i]=0
    else:
        x[i]=1
print(x)
    


# Nested list 
x = [[0,2],[8,"darshan"]]
# for i in x:
#     print(i,end="")



for i in x:
    if type(i) == list:
        for j in i:
            print(j)
        continue
    print(i)





student = [
    [101, "Ram", 98],
    [102, "Sita", 88],
    [103, "Rama", 87],
    [104, "Gita", 99]
]

for i in student:
    print(i[0])

sid = int(input("Enter ID: "))
name = input("Enter Name: ")
marks = int(input("Enter Marks: "))

student.append([sid, name, marks])

print("\nUpdated Student List:")
for i in student:
    print(f"{i[1]}-->{i[2]}")


















