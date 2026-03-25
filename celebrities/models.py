from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Celebrity(models.Model):
    full_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='celebrities/', null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self): return self.full_name
