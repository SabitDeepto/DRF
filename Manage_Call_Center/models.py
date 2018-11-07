from django.db import models


# Create your models here.
class CreateExecutive(models.Model):
    executive_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.executive_name
