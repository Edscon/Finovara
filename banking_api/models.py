from django.db import models
from users.models import Account
# Create your models here.

class Institutions(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    bic = models.CharField(max_length=20)
    transaction_total_days = models.PositiveIntegerField()
    max_access_valid_for_days = models.PositiveIntegerField()
    logo = models.URLField()
    countries = models.JSONField()

    def __str__(self):
        return self.name
    
class BankAccount(models.Model):
    account = models.ForeignKey(Account, related_name='bank_accounts', on_delete=models.CASCADE)
    bank = models.ForeignKey(Institutions, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=34)  # IBAN
    alias = models.CharField(max_length=100, blank=True, null=True)
    #balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, default='EUR')

    class Meta:
        unique_together = ('account', 'account_number')  # Un mismo usuario no debe tener 2 veces el mismo IBAN

    def __str__(self):
        return f'{self.account_number} ({self.bank.name})'
    
#Si se quisiera implementar guardar transacciones:
# class Transaction(models.Model):
#     bank_account = models.ForeignKey(BankAccount, related_name='transactions', on_delete=models.CASCADE)
#     transaction_id = models.CharField(max_length=50, unique=True)
#     date = models.DateTimeField()
#     amount = models.DecimalField(max_digits=12, decimal_places=2)
#     currency = models.CharField(max_length=3, default='EUR')
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.transaction_id} - {self.amount} {self.currency} on {self.date}'