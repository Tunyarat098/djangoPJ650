from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=200, default="")

    def __str__(self):
        return str(self.id) + " : " + self.name + ":" + self.desc


class Product(models.Model):
    pid = models.CharField(max_length=13, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    brand = models.CharField(max_length=50, default="")
    price = models.FloatField(default="0.00")
    net = models.IntegerField(default="0")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.pid + ":" + self.name + ":" + self.brand + ":" + \
            str(self.price) + ":" + str(self.net) + ":" + self.category.name


import datetime


class Employee(models.Model):
    eid = models.CharField(max_length=5, default="", )
    name = models.CharField(max_length=35, default="", )
    surname = models.CharField(max_length=35, default="", )
    address = models.CharField(max_length=200, default="", )
    gender = models.BooleanField(default=True)
    birthdate = models.DateField(default=datetime.date.today())
    salary = models.FloatField(default=0.00)

class testEmployee(models.Model):
    empid = models.CharField(max_length=13, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    address = models.TextField(max_length=200, default="")
    status = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=50, default="")
    salary = models.FloatField(default=0.00)
    gender = models.CharField(max_length=10, default="")
    birthday = models.DateField(default=None)
    born = models.CharField(max_length=30)
    marries = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ":" + self.name + "(" + self.status + ")"


class myProduct():
    def __init__(self, id, name, brand, type, flavor, amount, price, member):  # เพิ่ม type flavor amount

        self.__id = id
        self.__name = name
        self.__brand = brand
        self.__type = type
        self.__flavor = flavor
        self.__amount = amount
        self.__price = price
        self.__member = member
        self.__setDiscount()
        self.__setSum()
        self.__setTotal()

    def __setSum(self):
        self.__setSum = self.__price * self.__amount

    def __setDiscount(self):
        if self.__member == "yes":
            self.__discount = 100
        else:
            self.__discount = 0

    def __setTotal(self):
        self.__total = self.__setSum - self.__discount

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getBrand(self):
        return self.__brand

    def getType(self):
        return self.__type

    def getFlavor(self):
        return self.__flavor

    def getAmount(self):
        return self.__amount

    def getPrice(self):
        return self.__price

    def getMember(self):
        return self.__member

    def getDiscount(self):
        return self.__discount

    def getTotal(self):
        return self.__total
