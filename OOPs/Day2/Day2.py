"""
How to create a methods in a class

we have to define = @classmethod in this 

"""
class demo:
    # class variable | ins as institute
    ins = "Hello"
    # class method
    @classmethod
    def greet(cls):
        # print("Hello how are u?")
        return "Hi"
    
    @classmethod
    def modify(cls,new_value):
        cls.ins = new_value
        new_value= "Linkcdoe"


print(demo.greet())
print(demo.ins)
print(demo.ins)


# ===============================================

class demo:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age

    # ins method 
    def welcome(self):
        return "Hello Students !"
    
    def modify(self):
        newvalue = input("Enter new name: \n")
        ex_name = self.name
        self.name = newvalue
        print(f"Existing name {ex_name} -- Updated name {newvalue}")


s1 = demo("Ram", 101, 18)
print(s1.name,s1.id,s1.age)
print(s1.welcome())
s1.modify()


# =====================================================
