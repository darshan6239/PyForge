class car:
    def __init__(self):
        print("Mercedes")

    def __init__(self,name,model,wheels,price,available_car):
                self.name = name
                self.model = model
                self.wheels = wheels
                self.price = price
                self.available_car = available_car

car1 = car("A-Class", "GLS-A", "4-Wheels", 200, 6)
car2 = car("C-Class", "C220d", "4-Wheels", 300, 4)
car3 = car("E-Class", "C440d", "4-Wheels", 400, 2)
car4 = car("S-Class", "S550-D", "4-Wheels", 600, 7)
car5 = car("G-Wagon", "G-Wagon-D", "4-Wheels", 800, 1)

x = [car1,car2,car3,car4,car5]
total = 0
for i in x:
       total += i.price*i.available_car
print(f"Total Avaible balance: {total}")
       
# To call instead of using the printing statment again and again 
for i in x:
       print(i.name,i.model,i.wheels,i.price,i.available_car)

for i in x:
       if 5<i.available_car<10:
              print(i.name,i.available_car) 