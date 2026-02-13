from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    marks=models.FloatField()
    profile_image = models.ImageField(upload_to='students/', null= True, blank=True)

    def __str__(self):
        return self.name