# Generated by Django 5.0.4 on 2024-06-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_tournament_enrollment_fee_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='enrollment_fee',
            field=models.DecimalField(decimal_places=2, default=200, max_digits=10),
            preserve_default=False,
        ),
    ]
