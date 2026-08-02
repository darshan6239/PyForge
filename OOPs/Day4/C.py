from B import P
class C(P):
    prq = "bye"
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks = marks


obj = C("ram",21,90)
print(obj.prq,obj.xyz,obj.abc)
print(obj.name,obj.age,obj.marks)