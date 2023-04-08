from django.db import models

# Create your models here.
class Rencontre(models.Model):
    """
    rencontre model
    """
    codecoupon = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)

    class Meta:
        """meta
        """
        ordering = ['codecoupon']



        