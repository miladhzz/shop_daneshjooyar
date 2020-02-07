from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/product/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        ordering = ('create_time',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product', args=[self.id])


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    product_count = models.PositiveIntegerField()
    product_cost = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return str(self.id)


class Invoice(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    invoice_date = models.DateTimeField(auto_now_add=True)
    authority = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('failed', 'Failed'),
        ('completed', 'Completed')
    )
    invoice = models.ForeignKey(Invoice, null=True, on_delete=models.SET_NULL)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return str(self.id)
