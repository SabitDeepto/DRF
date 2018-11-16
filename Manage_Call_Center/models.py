from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models.signals import post_save

from Manage_Merchants.models import PickUp


class CreateExecutive(models.Model):
    executive_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.executive_name


# signals from User to model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


# signals from User to model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


# signals from model to model (merchant to call center )

class HandleRequest(models.Model):
    user = models.OneToOneField(PickUp, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = HandleRequest.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=PickUp)