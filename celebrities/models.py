from django.db import models

class Celebrity(models.Model):
    full_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.full_name
    photo = models.ImageField(upload_to='celebrities/', null=True, blank=True)