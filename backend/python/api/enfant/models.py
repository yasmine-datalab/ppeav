from django.db import models

# Create your models here.

class Enfant(models.Model):
    """
        define child model
    """
    matricule = models.CharField(max_length=50, blank=False, primary_key=True)
    nom = models.CharField(max_length=50, blank=False)
    prenom = models.CharField(max_length=50, blank=False)
    sexe = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    vulnerabilite = models.CharField(max_length=50)

    class Meta:
        """
        meta
        """
        ordering = ['nom']
