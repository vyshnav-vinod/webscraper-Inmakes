from django.db import models

# Create your models here.


class Links(models.Model):
    address = models.TextField(max_length=500, null=True, blank=True)
    name = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.address
