""" To reverse the string without inbuilt functions"""

x = "Hello"
rev = ""
for ch in x:
    rev = ch+rev
print(rev)


# Duplicate char remove --hello = l --> helo
z = "Hello"
op = ""
for ch in z:
    if ch not in op:
        op+=ch
print(op)


# there is a string we have to tell how many characters are there 
a = "i like python programming"
words = a.split()
print(words)
print(len(words))


# Count the number of words in it 
str1 = "Python_is_easy_to_learn"
word = str1.split("_")
print(word)
print(len(word))


# find largest word in string ? 

str2 = "Python is interpreted language "
word = str2.split()
largest_word = ""
for ch in word:
    if len(ch) > len(largest_word):
        largest_word = ch
print(largest_word)


# Hello --> h:1 e:1 l:2 o:1
str3 = "Hello"
freq = {}
for ch in str3:
    if ch in freq:
        freq += 1
    else:
        freq -= 1
print(freq)



# LIST !  --->Mutable 
"""     List are mutable 
        Array is used internally 
        0 -->Index starting 
        1--> size 
        [,] --> Comma is being used for seperation 

        """

rollno = [101,102,103]
print(rollno[0])

#--------------------------------------------

student_name = ["abc", "xyz", "pqr", "mno"]
print(student_name)

print(student_name[1])
print(student_name[-1])


#--------------------------------------------
"Mixed Values"

mixed = [1, 90.99, "ram", 2, 89.87, "shyam"]
print(mixed)
print(mixed[2])

print(mixed[-2])

# We can change the stign value 
mixed[2] = "ramesh"
print(mixed)
print(type(mixed))

#list loop 
for i in mixed:
    print(i)

# adding a element in list
"""There are two ways 1) append - which gets add in the last 
                      2) insert(indexno, value) - add at the particular index value """
x = [10,20,30,40,50]
x.append(60)
print(X)
x.insert(2,100)
print(x)


#remove : 1) remove(element) 2) Pop(index)
x.remove(20)
print(x)
x.pop(4)
print(x)

""" 
Homework
1) Q = [24,56,78,97,30]

-- Even print
-- odd element -->sum
-- %5 --> sq --> cube 
--> Reverese 
--> even --> 0 | odd --> 1 [0,0,0,1,0]
"""



# HOmework 

a=[24,56,78,97,30]
#1.Even print
for i in a:
    if i%2==0:
      print (i)
      
#2.odd element sum
a=[24,56,78,97,30]
sum=0
for i in a:
    if i%2!=0:
        sum=sum+i
        print(sum)
        
#3.%5->square->cube
a=[24,56,78,97,30]
square = 0
for i in a:
    if i%5==0:
        square = i**2
print(square**3)
        
#4.Reverse
a=[24,56,78,97,30]
print(a[::-1])

#5.even->0 odd->1
a=[24,56,78,97,30]
result=[]
for i in a:
    if i%2==0:
        result.append(0)
    else:
        result.append(1)
print(result)