# Generated by Django 5.0.3 on 2025-06-01 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banking_api', '0002_bankaccount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BankAccount',
        ),
    ]
