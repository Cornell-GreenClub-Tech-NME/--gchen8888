from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.TextField()
    username = models.TextField()
    balance = models.FloatField()
   

    def __str__(self):
        return self.name
    
# TODO: Create Transaction Model
class Transaction(models.Model):
    id = models.TextField(primary_key=True) 
    amount = models.FloatField()
    senderid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='senderid')
    receiverid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiverid')
    pending = models.BooleanField()

     # TODO: Create relationship to Transaction model
    #user = models.ForeignKey(User, on_delete=models.CASCADE)