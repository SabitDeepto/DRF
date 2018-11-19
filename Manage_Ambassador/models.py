from django.db import models


# admin can register merchant
class CreateAmbassador(models.Model):
    ambassador_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.ambassador_name