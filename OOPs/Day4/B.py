from A import GP
class P(GP):
    abc = "hey"

    def __init__(self,name,age):
        super().__init__(name)
        self.age = age