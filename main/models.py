from django.db import models

# Create your models here.


class Sponsor(models.Model):
    TYPE_CHOICES = [
        ('Type 1', 'Type 1'),
        ('Type 2', 'Type 2'),
        ('Type 3', 'Type 3'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='sponsors/')

    def __str__(self):
        return self.name
