from django.db import models

# Create your models here.
class rencontre(models.Model):
    codecoupon = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=15, decimal_places=2)
    latitude = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        ordering = ['codecoupon']