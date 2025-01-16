import uuid

from django.db import models


# Create your models here.
class UserInformation(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=64, unique=True)
    annual_income = models.FloatField()
    aadhar_id = models.CharField(max_length=64, unique=True)
    credit_score = models.IntegerField(default=0)
    user_uuid = models.UUIDField(default=uuid.uuid4, unique=True)

class UserTransactionInformation(models.Model):
    TRANSACTION_TYPES = [("CREDIT", "Credit"), ("DEBIT", "Debit")]

    aadhar_id = models.CharField(max_length=64)
    registration_date = models.DateTimeField(auto_now_add=False)
    amount = models.FloatField(default=0.0)
    transaction_type = models.CharField(max_length=8, choices=TRANSACTION_TYPES)
