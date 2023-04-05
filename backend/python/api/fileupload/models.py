from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_model(value):
    if value.lower() not in ["enfant", "structure", "rencontre"]:
        raise ValidationError(
            _('%(value)s is not a good model'),
            params={'value': value},
        )
def validate_file(value):
    if (not value.lower().endswith("csv")):
        raise ValidationError(
            _('%(value)s is not an excel file'),
            params={'value': value},
        )
CHILDREN = "ENFANT"
STRUCTURE = "STRUCTURE"
RENCONTRE = "POINT DE RENCONTRE"

class CSVFile(models.Model):
    """
    
    """
    TYPES = (
        (CHILDREN, "ENFANT"),
        (STRUCTURE, "STRUCTURE"),
        (RENCONTRE, "POINT DE RENCONTRE")

    )
    model = models.CharField(max_length=20,blank=False, choices= TYPES, null= False)
    file = models.FileField(verbose_name="csv File", upload_to=f'{model}_files', validators=[validate_file]) 

    class Meta:
        ordering = ['file']