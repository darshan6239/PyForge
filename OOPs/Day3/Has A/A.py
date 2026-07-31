class engine:
    # class var
    brand = "BMW"
    def __init__(self,horsepower):
        # ins var manually declare 
        self.name = "V8"
        # user ip --> when oobj get created at that time user will send some ip
        self.horsepower = horsepower

    def show_engine(self): # instance method
        return f"Engine Details are: {self.brand}\n{self.horsepower}\n{self.name}"



