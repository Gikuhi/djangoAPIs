from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, default="john doe")
    number = models.IntegerField()
    gender = models.CharField(max_length=6)
    image = models.ImageField(upload_to='images', default="profiles/default.jpg")

class Student(models.Model):
    name = models.CharField(max_length=100, default="john doe")
    age = models.IntegerField()
    grade = models.CharField(max_length=2, default="C1")


    # backend specifying the customer via name

    def __str__(self):
        return self.name


