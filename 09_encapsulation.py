class Computer:
    def __init__(self):
        self.brand = "Apple"
        self.model = 2017
        self.price = 150000

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    # Setters are used to set the values of the attributes

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price


computer = Computer()
print(computer.get_brand())
print(computer.get_model())
print(computer.get_price())

computer.set_brand("Dell")
computer.set_model(2020)
computer.set_price(100000)

print(computer.get_brand())
print(computer.get_model())
print(computer.get_price())
