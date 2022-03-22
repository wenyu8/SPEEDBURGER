from django.db import models
from django.utils import timezone


class User(models.Model):

    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=20, null=True)
    userId = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.firstName


class Product(models.Model):

    productName = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    calories = models.IntegerField()
    productID = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.productName)


class OrderDetail(models.Model):

    orderId = models.IntegerField(primary_key=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()
    firstName = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    status = models.CharField(max_length=20, null=True)
    order_timestamp = models.DateTimeField(null=True)
    amount = models.IntegerField()
    address = models.TextField(null=True)

    def __str__(self):
        return str(self.orderId)


class Order(models.Model):

    orderId = models.IntegerField(primary_key=True)
    productID = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, related_name='orderdetails')
    orderTotal = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.userId)


class Email(models.Model):
    email = models.CharField(max_length=100, null=True)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderid')
    orderTotal = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userid')

    def __str__(self):
        return str(self.userId)
