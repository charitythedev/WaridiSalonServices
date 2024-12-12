from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    # Constructor to return one of the values
    def __str__(self):
        return self.name

class Salon(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Salonist(models.Model):
    name = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    joiningDate = models.DateField(max_length=20)
    salon = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Pricing(models.Model):
    packageName = models.CharField(max_length=20)
    price = models.IntegerField()
    currency = models.CharField(max_length=20)

    def __str__(self):
        return self.packageName


class Service(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    price = models.ForeignKey(Pricing, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ContactRequest(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
