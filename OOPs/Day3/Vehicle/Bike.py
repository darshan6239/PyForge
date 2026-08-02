from Vehicle import vehicle


class Bike(vehicle):
    def __init__(self,fuel_type,brand,color,price):
                # ("petrol","BMW","black",5000)
        self.color = color
        self.price = price
        super().__init__(fuel_type,brand) # Parent calling 


    def ride(self):
        return "Bike ride so fast !"


    def custom_start(self):
        # calling parent mumber by using super()
        print(super().start())
        return "BRHHUUUUMMMMMMMM!!!!!"
    
    def avr(self):
        distance = int(input("Enter total distance in km: "))
        petrol = int(input("Enter petrol used in ltr: "))
        self.avrerage = distance/petrol
        print(f"Average Mileage: {self.avrerage} km/l")
        return self.avrerage

    
b1 = Bike("petrol","BMW","black",5000)
# print(b1.color)
# print(b1.fuel_type)


# print(b1.custom_start())
# print(b1.ride())
# print(b1.stop())


avg = b1.avr()
