# Generated by Django 5.1.5 on 2025-01-16 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_service', '0002_rename_user_userinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='email',
            field=models.EmailField(max_length=64, unique=True),
        ),
    ]
