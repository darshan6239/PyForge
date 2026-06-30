#   DICTIONARY 

"""
used to stored data in key value pair 
key should be unique 
value_duplicate
{}
"""
# x = {}
# print(x, type(x))
# # add --> refvar[key] = value
# x["Roll no"] = "Ram"
# print(x)


# # access ---> x[key] ---> value
# print(x["name"])

# # update ---> ref[key] ---> new value
# x["name"] = "sita"
# print(x["name"])


# instead of = we use : in dictionary 
stud = {
    "rollno":101,
    "name":"ram",
    "age":30,
    "sub":["math","eng","java"],
    "marks":(90,89,67)
}
# print(stud)

# # methods 
# print(stud.keys())
# print(stud.values())
# print(stud.items())

# loops 
# for key in stud:
#     print(key)          # to access all the keys

# for values in stud.values():
#     print(values)           # to access the values 

# for k,v in stud.items():
#     print(k,v)

"to print subjects seperately "
for keys in stud:
    if keys == "sub":
        for i in stud[keys]:
            print(i)

" to print in defined form "
for i in range(len(stud["sub"])):
    print(f"{stud["sub"][i]} --> {stud["marks"][i]}")

#   using function =  zip function (combines multiple loop values to print it in one)
for sv , mv in zip(stud["sub"], stud["marks"]):
    print(sv, mv)






stud = {
    101:{
    "rollno":10,
    "name":"ram",
    "age":21,
    "sub":["math","eng","java"],
    "marks":(90,89,67)
    },
    102:{
    "rollno":11,
    "name":"sita",
    "age":24,
    "sub":["math","eng","java"],
    "marks":(99,80,77)
    },
    103:{
    "rollno":12,
    "name":"shyam",
    "age":33,
    "sub":["math","eng","java"],
    "marks":(97,59,66)
    }
}

print(stud[101]["sub"][2])


for key in stud[101].keys():
    print(key)




# to print marks from the list 
for key in stud:
    for v in stud[key]["marks"]:
        print(v, end=" ")
    print("\n")


for key in stud:
    print(f"=====Student Id =====")
    for key,value in stud[key].items():
        print(f"{key} : {value}")



""" 
1) ADD STUDENT -- USer 
2) EACH STUDENT -- TOTAL MARKS ---> SUM
                -- PERCENTAGE 
3) EACH SUBJECT -- Topper of each subject (Java, Maths, English)
                   Lower of each subject (Java, Maths, English )

"""

# x = {}
# print(x, type(x))
# # add --> refvar[key] = value
# x["Roll no"] = "Ram"
# print(x)

print("========= Student Marks System ========== ")
stud = {}
while True:
    print("1. Enter Student Details \n2. View Student Details \n3. View the TOPPERS \n4. View the LOOSERS")
    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            while True:
                stud_name = input("Please Enter Student Details: ")
                stud_rollno = input("Please Enter Student Roll number: ")
                Subjects = []
                subjet_marks = []
                n = int(input("How many subjects does the student have: "))
                for i in range(n):
                    stud_sub = input(f"Please Enter Student's Subject {i+1}: ")
                    Subjects.append(stud_sub)      
                    stud_marks = int(input(f"Please ENter student Subject {i+1} Marks: "))
                    subjet_marks.append(stud_marks)
            
                stud[stud_rollno] = {
                    "Student Name" : stud_name,
                    "Roll no" : stud_rollno,
                    "Subjects" : Subjects,
                    "Marks" : subjet_marks
                }

                ct = int(input("Press 1 if you want to continue else press 0: "))
                if ct == 0:
                    break

        case 2:
            overall = int(input("1. Overall Data\n 2. Only Subjects\n 3. Only Marks\n 4. Subjects with marks"))
            match overall:
                case 1:
                    for items in stud.items():
                        print(items)
                case 2:
                    for items in stud.values():
                        print(items["Subjects"])

                case 3:
                    for items in stud.values():
                        print(items["Marks"])

                case 4:
                    for key in stud:
                        subjects = stud[key]["Subjects"]
                        marks = stud[key]["Marks"]

                        print("Subjects with Marks")
                        for sub, mark in zip(subjects, marks):
                            print(f"{sub} --> {mark}")

        case 3:
            topper = None
            highest = 0

            for key in stud:
                total = sum(stud[key]["Marks"])

                if total > highest:
                    highest = total
                    topper = stud[key]

            print("\n===== TOPPER =====")
            print("Student Name :", topper["Student Name"])
            print("Roll No :", topper["Roll no"])
            print("Marks :", topper["Marks"])
            print("Total :", highest)

        case 4:
            loser = None
            lowest = float('inf')

            for key in stud:
                total = sum(stud[key]["Marks"])

                if total < lowest:
                    lowest = total
                    loser = stud[key]

            print("\n===== LOSER =====")
            print("Student Name :", loser["Student Name"])
            print("Roll No :", loser["Roll no"])
            print("Marks :", loser["Marks"])
            print("Total :", lowest)

        case 5:
            break


# split() Method is used ! 


