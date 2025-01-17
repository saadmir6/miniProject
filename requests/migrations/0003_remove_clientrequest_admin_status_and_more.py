# Generated by Django 5.1.2 on 2024-10-29 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_clientrequest_admin_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientrequest',
            name='admin_status',
        ),
        migrations.RemoveField(
            model_name='clientrequest',
            name='finance_status',
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_time', models.DateTimeField()),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='requests.clientrequest')),
            ],
        ),
    ]
