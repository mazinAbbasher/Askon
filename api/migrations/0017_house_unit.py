# Generated by Django 5.1.4 on 2025-01-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_house_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='unit',
            field=models.CharField(default='متر', max_length=50),
        ),
    ]
