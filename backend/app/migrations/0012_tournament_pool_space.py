# Generated by Django 5.0.4 on 2024-07-04 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_mpesatransaction_is_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='pool_space',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournaments', to='app.poolspace'),
        ),
    ]
