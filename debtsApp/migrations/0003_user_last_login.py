# Generated by Django 4.2 on 2023-04-14 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debtsApp', '0002_debtor_user_alter_debt_debtor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
