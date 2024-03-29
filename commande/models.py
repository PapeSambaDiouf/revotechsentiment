from django.db import models
from client.models import Client
from produit.models import Produit

# Create your models here.
class Commande(models.Model):
    objects = None
    STATUS = (('en instance', 'en instance'),
              ('non livré', 'non livré'),
              ('livré', 'livré'))

    # DEBUT CREATION DE RELATION ONE TO MANY
    client = models.ForeignKey(Client, null=True,on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    # END DE LA RELATION ONE TO MANY
    status = models.CharField(max_length=200, choices = STATUS, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)