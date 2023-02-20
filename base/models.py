from django.db import models

# Create your models here.

class Advocate(models.Model):
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null = True, blank = True)
    username = models.CharField(max_length=20)
    bio = models.TextField(max_length=150, null = True, blank = True)

    def __str__(self):
        return self.username


class Company(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=150, null = True, blank = True)

    def __str__(self):
        return self.name
