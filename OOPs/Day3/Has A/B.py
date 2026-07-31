from A import engine
class car:
    def __init__(self,uip):
        self.age = 90
        # object inject 
        self.a = engine(uip)

    def car_details(self):
        print(self.a.show_engine())
        return f"Car details are: {self.age}"

obj = car(200)
print(obj.age , obj.a.name, obj.a.horsepower)
print(engine.brand)


# method calling 
print(obj.car_details())
print(obj.a.show_engine())
