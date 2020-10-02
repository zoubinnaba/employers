from django.db import models

class Employer(models.Model):
    nom = models.CharField(max_length=255, null=False)
    prenom = models.CharField(max_length=225, null=False)
    numero_de_telephone = models.CharField(max_length=255, null=False)
    biographie = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = "employer"

    def __str__(self):
        return f"{self.nom}"

