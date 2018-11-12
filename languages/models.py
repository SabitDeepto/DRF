from django.db import models


# Create your models here.
class Type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Language(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.name