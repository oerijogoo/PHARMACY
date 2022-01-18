from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Stimulant', 'Stimulant'),
    ('Antiviral', 'Antiviral'),
    ('Depressant', 'Depressant'),
)


class Drug(models.Model):
    drug = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    name = models.ForeignKey(Drug, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'
