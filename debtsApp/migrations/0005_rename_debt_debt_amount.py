# Generated by Django 4.2 on 2023-04-14 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debtsApp', '0004_remove_debtor_user_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debt',
            old_name='debt',
            new_name='amount',
        ),
    ]
