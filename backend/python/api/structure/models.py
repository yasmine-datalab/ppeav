from django.db import models

# Create your models here.

class Structure(models.Model):
    """
        structure model
    """
    id = models.AutoField(primary_key=True)
    structure = models.CharField(max_length=200, blank=False)
    sigle = models.CharField(max_length=100, blank=False)
    type = models.CharField(max_length=100, blank=False)
    telephone = models.CharField(max_length=50, blank=False)
    adresse = models.CharField(max_length=100, blank=False)
    commune = models.CharField(max_length=100, blank=False)
    localisation = models.CharField(max_length=100, blank=False)
    domaine_intervention = models.CharField(max_length=100, blank=True)
    GPS =  models.CharField(max_length=100, blank=True)

    class Meta:
        """
        meta"""
        ordering = ['structure']