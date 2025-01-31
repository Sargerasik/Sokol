from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Material(models.Model):
    material = models.CharField(max_length=100, primary_key=True)

class Category(models.Model):
    category = models.CharField(max_length=124)

class Product(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=124)
    articul = models.IntegerField()
    description = models.CharField(max_length=1000)
    image = models.ImageField()
    material = models.ForeignKey(to=Material, on_delete=models.SET_NULL, null=True)
    category= models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="avatar.png")
    birthday = models.DateField(null=True)
    cart = models.ManyToManyField(to=Product, related_name="client")
    favourites = models.ManyToManyField(to=Product, related_name="user")

    def __str__(self):
        return self.user.username



