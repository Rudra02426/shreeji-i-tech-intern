from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    address = models.CharField(max_length=150, blank=True, null=True)
    course = models.CharField(max_length=50, blank=True, null=True)
    marks = models.FloatField()
    profile_image = models.ImageField(upload_to='students/', null=True, blank=True)

    def save(self, *args, **kwargs):

    # Auto-create user if not linked
        if not self.user:

            username = slugify(self.name)

            # Ensure username is unique
            base_username = username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1

            default_password = "123@123@"

            user = User.objects.create_user(
                username=username,
                password=default_password
            )

            self.user = user

        # 🔥 THIS LINE WAS MISSING
        super().save(*args, **kwargs)




    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['id']

    @property
    def result(self):
        return "Pass" if self.marks >= 35 else "Fail"

    @property
    def percentage(self):
        return f"{self.marks}%"
