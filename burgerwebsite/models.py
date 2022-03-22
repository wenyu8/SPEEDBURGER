from django.db import models
from django.utils import timezone


class User(models.Model):

    userId = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.firstName


class Product(models.Model):
    productName = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField()
    calories = models.IntegerField()
    productID = models.IntegerField(max_length=50, primary_key=True)

    def __str__(self):
        return str(self.productName)


class OrderDetail(models.Model):

    orderId = models.IntegerField(primary_key=True)
    productID = models.ForeignKey(Product, null=True,on_delete=models.PROTECT)
    quantity = models.IntegerField(null=True)
    firstName = models.ForeignKey(User,null=True,on_delete=models.PROTECT)
    lastName = models.ForeignKey(User,null=True,on_delete=models.PROTECT)
    email = models.ForeignKey(User,null=True,on_delete=models.PROTECT)
    status = models.CharField(max_length=20,null=True)
    order_timestamp = models.DateTimeField(null=True)
    amount = models.IntegerField(null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return str(self.firstName)


class Order(models.Model):

    orderId = models.IntegerField(primary_key=True)
    productID = models.ForeignKey(OrderDetail, null=True,on_delete=models.PROTECT)
    orderTotal = models.DecimalField()
    userId = models.ForeignKey(User,null=True,on_delete=models.PROTECT)
    email = models.ForeignKey(User,null=True,on_delete=models.PROTECT)
    status = models.CharField(max_length=20,null=True)

    def __str__(self):
        return str(self.userId)


class Email(models.Model):

    orderId = models.ForeignKey(Order, null=True, on_delete=models.PROTECT)
    orderTotal = models.ForeignKey(Order, null=True, on_delete=models.PROTECT)
    userId = models.ForeignKey(User, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.userId)

