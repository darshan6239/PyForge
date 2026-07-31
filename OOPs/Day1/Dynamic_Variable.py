class mobile:
    def __init__(self,uname,ubrand,ucolor,uprice):
        self.name = uname
        self.brand = ubrand
        self.color = ucolor
        self.price = uprice # Parametrised 

# Obj
obj = mobile("Iphone15", "Iphone", "Black", "100")
print(obj.name, obj.color, obj.price)

obj1 = mobile("Iphone15", "Iphone", "Pink", "200")
print(obj1.name, obj1.color, obj1.price)


x = [obj, obj1]
for i in x:
    print(i.name)


