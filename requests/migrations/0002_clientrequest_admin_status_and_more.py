# Generated by Django 5.1.2 on 2024-10-29 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientrequest',
            name='admin_status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='finance_status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]