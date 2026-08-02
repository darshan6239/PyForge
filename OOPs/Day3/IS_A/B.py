from A import A 
class B(A):
    def abc(self):
        print("Hello abc")

    def __init__(self):
        print("Default constructor from B class")

obj = B()
print(obj.rollno)
# print(.abc)
# print(obj.xyz)
print(B.mro)

# method resolution order