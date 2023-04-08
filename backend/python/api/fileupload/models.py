from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


CHILDREN = "ENFANT"
STRUCTURE = "STRUCTURE"
RENCONTRE = "POINT DE RENCONTRE"


def validate_file(value):
    """
        if str endswith .csv
    """
    if not value.name.lower().endswith(".csv"):
        raise ValidationError(
            _('%(value)s is not a CSV file'),
            params={'value': value},
        )

class CSVFiles(models.Model):
    """
       csv
    """
    TYPES = (
        (CHILDREN, "ENFANT"),
        (STRUCTURE, "STRUCTURE"),
        (RENCONTRE, "POINT DE RENCONTRE")

    )
    model = models.CharField(max_length=20,blank=False, choices= TYPES, null= False)
    file = models.FileField(verbose_name="csv File", upload_to=f'{model}_files', validators=[validate_file])

    class Meta:
        """
        meta"""
        ordering = ['file']
