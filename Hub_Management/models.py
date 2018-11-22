from django.db import models


# Create Hub Manager
class CreateHubManager(models.Model):
    manager_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.manager_name


# Creating Zone wise hub list
class CreateHub(models.Model):
    hub_name = models.CharField(max_length=100)
    location = models.TextField()
    assigned_manager = models.ForeignKey(CreateHubManager, on_delete=models.CASCADE)

    class Meta:
        ordering = ('hub_name',)

    def __str__(self):
        return self.hub_name