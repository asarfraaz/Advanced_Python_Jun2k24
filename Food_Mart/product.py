'''
    Represents a product in inventory
'''

class Product:
    def __init__(self, name, quant, price):
        self.name = name
        self.quant = quant
        self.price = price

    def __repr__(self):
        return f'Product({self.name!r}, {self.quant}, {self.price})'

    def cost(self):
        return self.quant * self.price

    def sell(self, nunits):
        self.quant -= nunits
