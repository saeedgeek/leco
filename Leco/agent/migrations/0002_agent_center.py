# Generated by Django 3.0.4 on 2020-03-31 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('center', '0001_initial'),
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='center',
            field=models.ManyToManyField(related_name='agent', to='center.Center'),
        ),
    ]
