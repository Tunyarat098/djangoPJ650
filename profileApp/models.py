
class Product:
    def __init__(self, id, name, brand, price, net):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.net = net


    def __str__(self):
        return "ID:{}, Name:{}, Brand:{}, Price:{}, Net:{}".format(self.id, self.name, self.brand, self.price, self.net)
# Create your models here.
