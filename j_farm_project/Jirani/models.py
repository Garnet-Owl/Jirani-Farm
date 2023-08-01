from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Tractor(models.Model):
    owner = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='tractors')
    model = models.CharField(max_length=50)
    year = models.IntegerField( default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.model


class Lease(models.Model):

    tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE, related_name='leases')
    renter = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='leases')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20,
                              choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled'),
                                       ('completed', 'Completed')], default='pending')

    def __str__(self):
        return f'{self.tractor} - {self.renter}'
