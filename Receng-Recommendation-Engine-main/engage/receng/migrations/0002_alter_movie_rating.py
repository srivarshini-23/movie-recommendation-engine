# Generated by Django 4.0.4 on 2022-05-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
